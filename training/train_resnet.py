import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.models as models
from torch.utils.data import DataLoader, Dataset
import os
from PIL import Image
from tqdm import tqdm



# Activer le GPU
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"📌 Utilisation de : {DEVICE}")

# Configuration
IMG_SIZE = (200, 200)
BATCH_SIZE = 64  # Augmenté pour accélérer l'entraînement
EPOCHS = 100
DATASET_PATH = os.path.join(os.getcwd(), "dataset")  # 📌 Chemin relatif pour une exécution locale
MODEL_SAVE_PATH = os.path.join(os.getcwd(), "models", "resnet_anomaly_detector.pth")

# Optimisation GPU
torch.backends.cudnn.benchmark = True  # Optimisation pour NVIDIA GPU
# Définition des transformations (améliorées)
train_transform = transforms.Compose([
    transforms.Resize(IMG_SIZE),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(30),
    transforms.RandomAffine(degrees=0, translate=(0.2, 0.2), scale=(0.8, 1.2), shear=10),
    transforms.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4, hue=0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

val_transform = transforms.Compose([
    transforms.Resize(IMG_SIZE),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Définition du Dataset personnalisé
class AnomalyDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.data = []
        for label, category in enumerate(["normale", "anormale"]):
            category_path = os.path.join(root_dir, category)
            if not os.path.exists(category_path):
                continue
            for img_name in os.listdir(category_path):
                img_path = os.path.join(category_path, img_name)
                self.data.append((img_path, label))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_path, label = self.data[idx]
        image = Image.open(img_path).convert("RGB")
        if self.transform:
            image = self.transform(image)
        return image, torch.tensor(label, dtype=torch.long)

# Chargement des données
train_dataset = AnomalyDataset(os.path.join(DATASET_PATH, 'train'), transform=train_transform)
val_dataset = AnomalyDataset(os.path.join(DATASET_PATH, 'val'), transform=val_transform)

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)

# Définition du modèle ResNet50
model = models.resnet50(weights=None)
num_ftrs = model.fc.in_features
model.fc = nn.Sequential(
    nn.Dropout(0.4),
    nn.Linear(num_ftrs, 2048),
    nn.ReLU(),
    nn.Linear(2048, 2)
)
model = model.to(DEVICE)

# Définition de la fonction de perte et de l'optimiseur
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=5e-5, weight_decay=1e-4)  # Réduction du lr et ajout de weight decay
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.2, patience=3, verbose=True)

# Boucle d'entraînement
from torch.optim.lr_scheduler import ReduceLROnPlateau


for epoch in range(EPOCHS):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in tqdm(train_loader, desc=f"Epoch {epoch+1}/{EPOCHS}"):
        images, labels = images.to(DEVICE), labels.to(DEVICE)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        correct += (predicted == labels).sum().item()
        total += labels.size(0)

    train_loss = running_loss / len(train_loader)
    train_acc = correct / total

    # Validation
    model.eval()
    val_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            outputs = model(images)
            loss = criterion(outputs, labels)
            val_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)

    val_loss /= len(val_loader)
    val_acc = correct / total

    # Vérifier si on doit réduire le learning rate
    scheduler.step(val_loss)

    print(f"Epoch {epoch+1}/{EPOCHS} - Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f} - Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")

    # Sauvegarde du meilleur modèle
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        epochs_without_improvement = 0
        torch.save(model.state_dict(), "resnet_anomaly_detector.pth")  # Sauvegarde du meilleur modèle
    else:
        epochs_without_improvement += 1



# Sauvegarde du modèle sur Google Drive
torch.save(model.state_dict(), MODEL_SAVE_PATH)
print("Modèle sauvegardé")

