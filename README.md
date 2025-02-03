# AnomaCheck - Détection d'Anomalies Visuelles 🕵️‍♂️🔍 (Version Française)
AnomaCheck est une applicatiojnweb pour la détection automatique d'anomalies visuelles. Elle permet aux utilisateurs d'**uploader des images**, d'entraîner un modèle IA et de prédire si une image est normale ou anormale \
🚀 **Démo**:

## 📌 Fonctionnalités
✔ Upload d'images normales et anormales 🗂️ \
✔ Entraînement d'un modèle basé 🧠 \
✔ Prrédiction en temps réel des anomalies 🎯 \
✔ Stockage des fichiers et historique utilisateur 🗄️\
✔ Interface simple et accessible 🎨

## 📂Structure du Projet
```
AnomaCheck/ 
│── media/                  # Stockage des images uploadées
│── static/                # Fichiers statiques (CSS, images)
│   ├── css/
│   │   ├── base.css
│   │   ├── dashboard.css
│   │   ├── forgot_password_done.css
│   │   ├── forgot_password.css
│   │   ├── index.css
│   │   ├── login.css
│   │   ├── next_page.css
│   │   ├── password_reset_complete.css
│   │   ├── password_confirm.css
│   │   ├── register.css
│   │   ├── upload_page.css
│   │   ├── user_logout.css
│   ├── img/
│   │   ├── logo_1.png      # Logo
│── templates/              # Templates HTML pour Django
│   ├── home/
│   │   ├── base.html       # Page d'accueil
│   │   ├── upload_page.html # Page d'upload des images
│   │   ├── dashboard.html   # Tableau de bord
│   │   ├── forgot_password_done.html
│   │   ├── forgot_password.html
│   │   ├── login.html
│   │   ├── next_page.html
│   │   ├── password_reset_complete.html
│   │   ├── password_reset_confirm.html
│   │   ├── password_reset_email.html
│   │   ├── password_reset_subject.txt
│   │   ├── register.html
│   │   ├── user_logout.html
│── myapp/                 # Application Django principale 
│   ├── models.py           # Modèle des fichiers uploadés
│   ├── views.py            # Logique métier (upload, prédiction...)
│   ├── urls.py             # Routes du projet
│── manage.py               # Commandes Django
│── requirements.txt               # Commandes Django
│── README.md               # Ce fichier 🚀
```
## 🛠️ Installatione et Configuration
### 1️⃣ Cloner le dépot
```
git clone https://github.com/ton-utilisateur/AnomaCheck.git
cd AnomaCheck
```
### 2️⃣ Créer un environnement virtuel et installer les dépendances 
```
python -m venv venv
source venv/bin/activate # Sur macOS/Linux
venv\Scripts\activate # Sur Windows

pip install -r requirements.txt
```
### 3️⃣ Configurer les variable d'Environnement
Créer un fichier *.env* et ajoute : 
```
SECRET_KEY=ta_cle_secrete
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
```
### 4️⃣ Appliquer les migrations et créer un superutilisateur
```
python manage.py migrate
python manage.py createsuperuser
```
### 5️⃣ Lancer le serveur Django
```
python manage.py runserver
```
Accède a http://127.0.0.1:8000/ dans ton navigateur 

## 🎯 Utilisation
1️⃣ **Uploader des fichiers ZIP** contenant des images normales et anormales.
2️⃣ **Entraîner le modèle choisi** sur les images uploadées.
3️⃣ **Tester de nouvelles images** et voir si elles sont normales ou anormales.
4️⃣ **Accéder aux résultats**

## 🔗 Déploiement en ligne
Pour déployer sur **Railway** ou **Render**
```
pip install gunicorn whitenoise
git push origin main  # Envoie ton projet sur GitHub
```
Puis connecte ton dépot GitHub sur Railway ou Render

## 🎤 Contact 
📧 : charles.ndiaye@isen-ouest.yncrea.fr & mouhamed.dieng@isen-ouest.yncrea.fr
🌐 GitHub : ncharles11 & 

⭐️ N'oublie pas de laisser une étoile sur GitHub si ce projet t'a aidé !😉

# AnomaCheck - Detection of Visual Anomalies 🕵️‍♂️🔍 (English Version)
AnomaCheck is an applicatiojnweb for the automatic detection of visual anomalies. It allows users to **upload images**, train an AI model and predict whether an image is normal or abnormal\
🚀 **Demo**:

## 📌 Features
✔ Upload of normal and abnormal images 🗂️ \
✔ Training of a model based 🧠 \
✔ Real-time prediction of anomalies 🎯 \
✔ File storage and user history 🗄️\
✔ Simple, accessible interface 🎨

## 📂Project structure
```
AnomaCheck/ 
│── media/                  # Storage of uploaded images
│── static/                 # Static files (CSS, images)
│   ├── css/
│   │   ├── base.css
│   │   ├── dashboard.css
│   │   ├── forgot_password_done.css
│   │   ├── forgot_password.css
│   │   ├── index.css
│   │   ├── login.css
│   │   ├── next_page.css
│   │   ├── password_reset_complete.css
│   │   ├── password_confirm.css
│   │   ├── register.css
│   │   ├── upload_page.css
│   │   ├── user_logout.css
│   ├── img/
│   │   ├── logo_1.png      # Logo
│── templates/              # HTML templates for Django
│ ├── home/
│   │   ├── base.html       # Home page
│   │   ├── upload_page.html # Upload page
│   │   ├── dashboard.html   # Dashboard
│   │   ├── forgot_password_done.html
│   │   ├── forgot_password.html
│   │   ├── login.html
│   │   ├── next_page.html
│   │   ├── password_reset_complete.html
│   │   ├── password_reset_confirm.html
│   │   ├── password_reset_email.html
│   │   ├── password_reset_subject.txt
│   │   ├── register.html
│   │   ├── user_logout.html
│── myapp/                  # Main Django application 
│ ├── models.py             # Uploaded file model
│ ├── views. py             # Business logic (upload, prediction...)
│ ├── urls.py               # Project routes
│── manage.py               # Django commands
│── requirements.txt        # Django commands
│── README.md               # This file 🚀
```
## 🛠️ Installation and Configuration
### 1️⃣ Clone the repository
```git
clone https://github.com/ton-utilisateur/AnomaCheck. git
cd AnomaCheck
```
### 2️⃣ Create a virtual environment and install dependencies 
```
python -m venv venv
source venv/bin/activate # On macOS/Linux
venv\Scripts\activate # On Windows

pip install -r requirements.txt
```
### 3️⃣ Configure environment variables
Create a *. env* and add: 
```
SECRET_KEY=ta_cle_secrete
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
```
### 4️⃣ Apply migrations and create a superuser
```
python manage.py migrate
python manage. py createsuperuser
```
### 5️⃣ Launch Django server
```
python manage.py runserver
```
Access http://127.0.0.1:8000/ in your browser 

## 🎯 Usage
1️⃣ **Upload ZIP** files containing normal and abnormal images.
2️⃣ **Train the chosen template** on uploaded images.
3️⃣ **Test new images** and see if they are normal or abnormal.
4️⃣ **Access results**

## 🔗 Online deployment
To deploy on **Railway** or **Render**
```
pip install gunicorn whitenoise
git push origin main # Send your project to GitHub
```
Then connect your GitHub repository to Railway or Render

## 🎤 Contact 
📧 : charles.ndiaye@isen-ouest.yncrea.fr & mouhamed.dieng@isen-ouest.yncrea.fr 🌐
GitHub: ncharles11 & 

⭐️ Don't forget to leave a star on GitHub if this project helped you! 😉

