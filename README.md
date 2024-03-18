# Lecteur de Musique avec PyQt6

Ce projet consiste en la création d'un lecteur de musique interactif en utilisant PyQt6, une bibliothèque graphique multiplateforme pour Python. L'application permettra aux utilisateurs de charger, de lire, de mettre en pause et de gérer des fichiers audio, ainsi que de créer et de gérer des listes de lecture personnalisées. Le lecteur de musique offrira une interface utilisateur intuitive avec des fonctionnalités de contrôle audio et d'affichage des métadonnées des chansons en cours de lecture. Avec cette application, les utilisateurs pourront profiter de leur musique préférée tout en explorant une interface conviviale et esthétique.#### Interface Utilisateur :
1. **Boutons de Contrôle Audio** : Ajoutez des boutons pour jouer, mettre en pause, arrêter et sauter des pistes.
2. **Affichage du Titre de la Chanson** : Créez une zone d'affichage pour le titre de la chanson en cours de lecture.
3. **Liste de Lecture** : Utilisez un widget QListWidget pour afficher la liste de lecture.

#### Lecture Audio :
1. **Chargement des Fichiers Audio** : Utilisez la classe QMediaPlayer pour charger les fichiers audio.
2. **Fonctions de Contrôle de Lecture** : Implémentez des fonctions pour jouer, mettre en pause, arrêter et sauter des pistes.
3. **Gestion des Événements Audio** : Connectez les signaux audio (par exemple, le changement de piste) aux fonctions correspondantes.

#### Gestion de la Liste de Lecture :
1. **Ajout de Chansons** : Permettez aux utilisateurs d'ajouter des chansons à la liste de lecture.
2. **Suppression de Chansons** : Ajoutez des fonctionnalités pour supprimer des chansons de la liste de lecture.
3. **Sélection de Piste** : Connectez les éléments de la liste de lecture aux fonctions de lecture audio pour permettre aux utilisateurs de sélectionner des pistes à écouter.

#### Fonctionnalités Avancées (optionnel) :
1. **Recherche de Musique** : Implémentez une fonction de recherche pour permettre aux utilisateurs de trouver des chansons dans leur bibliothèque.
2. **Listes de Lecture Intelligentes** : Créez des listes de lecture basées sur les préférences de l'utilisateur (par exemple, les chansons les plus écoutées).
3. **Contrôles d'Égalisation Audio** : Intégrez des contrôles d'égalisation pour permettre aux utilisateurs de personnaliser leur expérience d'écoute.

### Instructions pour l'Implémentation

#### Interface Utilisateur :
1. Utilisez Qt Designer pour concevoir l'interface utilisateur avec les widgets nécessaires.
2. Enregistrez le fichier .ui généré par Qt Designer.

#### Lecture Audio :
1. Utilisez la classe QMediaPlayer pour gérer la lecture audio dans votre application.
2. Connectez les signaux audio (par exemple, `mediaPlayer.positionChanged`) aux fonctions de gestion d'événements dans votre code Python.

#### Gestion de la Liste de Lecture :
1. Utilisez QListWidget pour afficher la liste de lecture.
2. Ajoutez des boutons et des champs de texte pour permettre aux utilisateurs d'ajouter et de supprimer des chansons de la liste.

#### Fonctionnalités Avancées :
1. Implémentez des fonctions de recherche en utilisant les méthodes de filtrage de QListWidget.
2. Utilisez des algorithmes pour générer des listes de lecture intelligentes basées sur les données de lecture de l'utilisateur.
3. Intégrez des widgets d'égalisation audio dans votre interface utilisateur et utilisez les méthodes de QMediaPlayer pour ajuster les paramètres audio.
