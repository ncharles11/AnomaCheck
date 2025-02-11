# 📌 Plan du Rapport
## 1. Introduction
1.1. Contexte et Problématique
- Importance de la détection d'anomalies visuelles en contrôle qualité 
- Pourquoi utiliser l'intelligence artificielle pour automatiser ce processus 
- Présentation des différents modèles IA que nous allons tester 

1.2.  Objectifs du projet 
- Développer une **application web Django** qui permet : \
  ✅ L'upload d'images normales et anormales \
  ✅ Le choix entre plusieurs modèles IA pour la prédiction \
  ✅ L'entrainement et l'évaluation des modèles sur les images uploadées \
  ✅ La visualisation des résultats avec des graphiques

1.3 Organisation du rapport

## 2. État de l'art 
2.1. Méthodes de Détection d'Anomalies
- Explication des approches

2.2. Présentation des modèles IA utilisés

## 3. Cahier des charges
3.1. Expressions des besoins
- Besoins fonctionnels \
  ✔️ Sélection et entraînement du modèle IA \
  ✔️ Téléversement et stockage des images \
  ✔️ Interface utilisateur intuitive 
- Besoins non fonctionnels \
  ✔️ Performance \
  ✔️ Gestion des fichiers zip 

## 4. Architecture du Système
4.1. Architecture Générale
- Diagramme des composants : Backend, Modèles IA, Base de données

4.2. Schéma de la base de Base de données
- Modèle UploadedFile pour les images
- Modèle PredictionResult pour stocker les prédictions IA

4.3. Workflow de l'application \
1️⃣ Upload des images ZIP \
2️⃣ Sélectiondu modèle IA \
3️⃣ Détection des anomalies \
4️⃣ Affichage des résultats 

## Implémentation
5.1. Développement Backend (Django & API REST)
- Gestion des fichiers ZIP et validation
- Modèles de base de données

5.2. Intégration des modèles IA \
✅ EfficientNet-B4 \
✅ ResNet \
✅...

5.3. Développement Frontend (Django & Bootstrap)
- Page d'upload des fichiers
- Page de sélection du modèle IA
- Affichage des résultats sous forme de graphiques

## 6. Tests et Résultats 
6.1. Tests Unitaires et Fonctionnels
- Tests sur l'upload, la sélection des modèles et la prédiction

6.2. Analyses des Performances
| Modèle | Précision | Temps d'inférence| Taille du modèle|
|-----:|---------------|---------------|---------------|
|EfficientNet-B4|85%      |200 ms/image      |19M paramètres     |
|ResNet-50|      80%      |250 ms/image      |25M paramètres     |
|...|...               |...      |...     |

## 7. Conclusion et Perspectives
7.1. Bilan du Projet
- Résumé des résultats obtenus

7.2. Pistes d'amélioration \
✅ Déploiement en ligne \
✅ Optimisation GPU pour réduire le temps d'inférence \
✅ Ajout d'un mode AutoML pour choisir automatiquement le meilleur modèle

## 8. Bibliographie
