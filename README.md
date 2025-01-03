# Morpion_class
morpion avec des class
# Morpion - Tic Tac Toe

Un jeu de **Morpion** (Tic Tac Toe) avec une interface graphique développée en Python, utilisant la bibliothèque **Tkinter** pour l'interface utilisateur et permettant de jouer contre un **bot** ou un autre joueur en mode **multijoueur**.

## Fonctionnalités

- Mode **1 joueur** : Jouez contre un **bot** (facile ou difficile).
- Mode **2 joueurs** : Jouez avec un ami sur le même ordinateur.
- Choix du symbole : Choisissez entre **X** ou **O**.
- **Niveaux de difficulté du bot** : Le bot peut être en mode facile (choix aléatoire) ou difficile (algorithme de stratégie pour gagner ou bloquer).

## Prérequis

Avant de pouvoir lancer le jeu, vous devez avoir Python installé sur votre machine.

1. **Python 3.13.1** : Téléchargez et installez la dernière version de Python depuis [python.org](https://www.python.org/downloads/).
2. **Tkinter** : La bibliothèque Tkinter est incluse dans la plupart des installations de Python, mais si elle n'est pas installée, vous pouvez la récupérer via :

   - Pour Ubuntu/Debian :
     ```bash
     sudo apt-get install python3-tk
     ```
   - Pour macOS, Tkinter est inclus avec Python.
   - Pour Windows, Tkinter est généralement déjà installé avec Python.

## Installation

Clonez ce dépôt GitHub sur votre machine locale en utilisant Git ou téléchargez le fichier ZIP.

###Lancer le jeu
Accédez au dossier du projet
Ouvrez un terminal ou une invite de commande.
Déplacez-vous dans le répertoire du projet avec la commande suivante :
bash
Copier le code
````cd chemin/vers/le/dossier/morpion````
Lancer le jeu
Exécutez le fichier main.py pour démarrer l'application avec la commande suivante :

bash
Copier le code : ````python main.py````
Cela ouvrira la fenêtre graphique du jeu Tic Tac Toe.

###Interface de jeu
Une fois l'interface lancée, vous pourrez choisir le mode de jeu :

###Jouer contre le Bot : Vous pouvez jouer contre un bot. Le bot vous affrontera en choisissant entre le mode facile ou difficile.
Jouer à 2 joueurs : Vous pouvez jouer avec un autre joueur sur le même ordinateur.
Ensuite, vous choisissez votre symbole (X ou O).

Vous jouez ensuite en cliquant sur les cases du plateau. Le jeu met à jour l'interface après chaque coup et indique le vainqueur à la fin.

###Rejouer
Après chaque partie, un bouton "Rejouer" vous permet de recommencer une nouvelle partie.


