# Application d'Échecs Simpliste

### Description

Cette application est une implémentation simple d'un jeu d'échecs en utilisant Python et le framework PyQt6 pour l'interface graphique. L'objectif principal est de fournir une interface utilisateur conviviale pour jouer aux échecs contre un adversaire sur un même ordinateur.
Fonctionnalités
- Plateau d'échecs interactif avec interface graphique.
- Déplacement des pièces selon les règles classiques des échecs.
- Gestion des règles de jeu telles que l'échec, le pat et le mat.
- Possibilité de jouer contre un adversaire humain sur un même ordinateur.
- Interface utilisateur intuitive pour une expérience de jeu fluide.

### Conception

L'application suit une conception MVC (Modèle-Vue-Contrôleur) pour séparer la logique de présentation de la logique métier. Voici une vue d'ensemble de chaque composant :
- Modèle (Model) :
    - Représente l'état actuel du jeu, y compris la disposition des pièces sur le plateau.
    - Gère les règles du jeu et valide les mouvements des pièces.

- Vue (View) :
    - Interface utilisateur graphique réalisée avec PyQt6.
    - Affiche le plateau d'échecs et les pièces.
    - Gère les interactions utilisateur telles que le clic sur une pièce et le déplacement de celle-ci.

- Contrôleur (Controller) :
    - Gère les événements utilisateur et les actions associées.
    - Transmet les actions de l'utilisateur au modèle pour validation.
    - Met à jour la vue en fonction des changements de l'état du jeu.

### Installation

Pour exécuter l'application localement, vous aurez besoin des dépendances suivantes :
- Python 3.x
- PyQt6