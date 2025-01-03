import random
import tkinter as tk

color_yellow = "#ffde57"  # Couleur jaune pour le texte


class Board:
    def __init__(self, frame, mode, joueur_symbole, bot_symbole=None, bot_type=None):
        self.frame = frame
        self.mode = mode  # Le mode est soit 'bot', soit 'two_players'
        self.joueur_symbole = joueur_symbole
        self.bot_symbole = bot_symbole
        self.bot_type = bot_type  # "facile" ou "difficile"
        self.grille = ["-"] * 9
        self.joueur_actuel = joueur_symbole
        self.jeu_termine = False
        self.boutons = [[None for _ in range(3)] for _ in range(3)]

    def setup_game(self):
        """Met en place le plateau de jeu et démarre la partie"""
        for widget in self.frame.winfo_children():
            widget.grid_forget()

        self.label = tk.Label(self.frame, text=f"C'est au tour de {self.joueur_actuel}", font=("Consolas", 20),
                              background="#343434", foreground="white")
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")

        for row in range(3):
            for column in range(3):
                self.boutons[row][column] = tk.Button(self.frame, text="", font=("Consolas", 50, "bold"),
                                                      background="#343434", foreground="#4584b6", width=4, height=1,
                                                      command=lambda r=row, c=column: self.jouer_coup(r, c))
                self.boutons[row][column].grid(row=row + 1, column=column)

        self.rejouer_button = tk.Button(self.frame, text="Rejouer", font=("Consolas", 20), background="#343434",
                                        foreground="white", command=self.reset_game)
        self.rejouer_button.grid(row=4, column=0, columnspan=3, sticky="we")

        if self.mode == "bot" and self.joueur_actuel == self.bot_symbole:
            self.tour_du_bot()

    def jouer_coup(self, ligne, colonne):
        """Gère le coup joué par un joueur"""
        if self.jeu_termine or self.grille[ligne * 3 + colonne] != "-":
            return

        self.grille[ligne * 3 + colonne] = self.joueur_actuel
        self.boutons[ligne][colonne].config(text=self.joueur_actuel)

        vainqueur = self.verifier_vainqueur()
        if vainqueur:
            if vainqueur == "égalité":
                self.label.config(text="Égalité !", foreground=color_yellow)
            else:
                self.label.config(text=f"Le joueur {
                                  vainqueur} a gagné!", foreground=color_yellow)
            self.jeu_termine = True
        else:
            self.changer_joueur()
            if self.mode == "bot" and self.joueur_actuel == self.bot_symbole:
                self.tour_du_bot()

    def verifier_vainqueur(self):
        """Vérifie si un joueur a gagné ou si la partie est une égalité"""
        combinaisons = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combinaison in combinaisons:
            if self.grille[combinaison[0]] == self.grille[combinaison[1]] == self.grille[combinaison[2]] != "-":
                return self.grille[combinaison[0]]

        if "-" not in self.grille:
            return "égalité"

        return None

    def changer_joueur(self):
        """Change de joueur (X -> O ou O -> X)"""
        self.joueur_actuel = self.bot_symbole if self.joueur_actuel == self.joueur_symbole else self.joueur_symbole
        self.label.config(text=f"C'est au tour de {self.joueur_actuel}")

    def reset_game(self):
        """Réinitialise le jeu"""
        self.grille = ["-"] * 9
        self.joueur_actuel = self.joueur_symbole
        self.jeu_termine = False
        self.setup_game()

    def bot_facile(self):
        """Le bot facile choisit une case vide au hasard parmi celles disponibles."""
        coups_possibles = [i for i, case in enumerate(
            self.grille) if case == "-"]
        if coups_possibles:
            coup = random.choice(coups_possibles)
            self.jouer_coup(coup // 3, coup % 3)

    def bot_difficile(self):
        """Kenbot joue intelligemment pour gagner ou bloquer l'adversaire."""
        def trouver_meilleur_coup(joueur):
            combinaisons = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]
            ]
            for combinaison in combinaisons:
                valeurs = [self.grille[i] for i in combinaison]
                if valeurs.count(joueur) == 2 and valeurs.count("-") == 1:
                    return combinaison[valeurs.index("-")]
            return None

        # Kenbot essaie de gagner
        coup = trouver_meilleur_coup(self.bot_symbole)
        if coup is not None:
            self.jouer_coup(coup // 3, coup % 3)
            return

        # Kenbot essaie de bloquer l'adversaire
        coup = trouver_meilleur_coup(self.joueur_symbole)
        if coup is not None:
            self.jouer_coup(coup // 3, coup % 3)
            return

        # Sinon, joue sur une case libre aléatoire
        self.bot_facile()

    def tour_du_bot(self):
        """Fait jouer le bot en fonction de son type."""
        if self.bot_type == "facile":
            self.bot_facile()
        elif self.bot_type == "difficile":
            self.bot_difficile()
