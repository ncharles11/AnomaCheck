# AnomaCheck - Détection d'Anomalies Visuelles 🕵️‍♂️🔍
AnomaCheck est une applicatiojnweb pour la détection automatique d'anomalies visuelles. Elle permet aux utilisateurs d'**uploader des images**, d'entraîner un modèle IA et de prédire si une image est normale ou anormale
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
│── static/                 # Fichiers statiques (CSS, JS, images)
│── templates/              # Templates HTML pour Django
│   ├── home/
│   │   ├── index.html       # Page d'accueil
│   │   ├── upload_page.html # Page d'upload des images
│   │   ├── dashboard.html   # Tableau de bord
│   │   ├── dashboard.html   # Tableau de bord
│── myapp/ \                 # Application Django principale 
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
