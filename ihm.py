import tkinter as tk
from board import Board

# Définition des couleurs pour l'interface
color_gray = "#343434"
color_player = "#ff6347"  # Rouge tomate pour le joueur
color_bot = "#1e90ff"  # Bleu dodger pour le bot
color_text = "white"


class IHM:
    def __init__(self):
        """Initialisation de l'interface graphique principale."""
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.frame = tk.Frame(self.window, bg=color_gray)
        self.frame.pack(fill="both", expand=True)

    def start_game(self, mode, joueur_symbole, bot_type=None):
        """Démarre une nouvelle partie selon le mode choisi."""
        bot_symbole = "O" if joueur_symbole == "X" else "X"  # Le bot joue le symbole opposé
        self.board = Board(self.frame, mode, joueur_symbole,
                           bot_symbole, bot_type)
        self.board.setup_game()

    def mafenetre(self):
        """Crée le menu principal avec les boutons pour choisir le mode de jeu."""
        for widget in self.frame.winfo_children():
            widget.destroy()

        label_mode_jeu = tk.Label(
            self.frame,
            text="Choisissez votre mode de jeu",
            font=("Consolas", 20),
            background=color_gray,
            foreground=color_text,
        )
        label_mode_jeu.grid(row=0, column=0, columnspan=3, sticky="we")

        bot_button = tk.Button(
            self.frame,
            text="Jouer contre le Bot",
            font=("Consolas", 20),
            bg=color_gray,
            fg=color_text,
            command=lambda: self.demander_symbole("bot"),
        )
        bot_button.grid(row=1, column=0, columnspan=3, sticky="we")

        two_players_button = tk.Button(
            self.frame,
            text="Jouer à 2 joueurs",
            font=("Consolas", 20),
            bg=color_gray,
            fg=color_text,
            command=lambda: self.start_game("two_players", "X"),
        )
        two_players_button.grid(row=2, column=0, columnspan=3, sticky="we")

    def demander_symbole(self, mode):
        """Permet au joueur de choisir son symbole (X ou O)."""
        for widget in self.frame.winfo_children():
            widget.destroy()

        label = tk.Label(
            self.frame,
            text="Choisissez votre symbole",
            font=("Consolas", 20),
            bg=color_gray,
            fg=color_text,
        )
        label.grid(row=0, column=0, columnspan=3, sticky="we")

        x_button = tk.Button(
            self.frame,
            text="Jouer en tant que X",
            font=("Consolas", 20),
            bg=color_player,
            fg=color_text,
            command=lambda: self.demander_type_bot(mode, "X"),
        )
        x_button.grid(row=1, column=0, columnspan=3, sticky="we")

        o_button = tk.Button(
            self.frame,
            text="Jouer en tant que O",
            font=("Consolas", 20),
            bg=color_bot,
            fg=color_text,
            command=lambda: self.demander_type_bot(mode, "O"),
        )
        o_button.grid(row=2, column=0, columnspan=3, sticky="we")

    def demander_type_bot(self, mode, joueur_symbole):
        """Permet au joueur de choisir le niveau de difficulté du bot."""
        for widget in self.frame.winfo_children():
            widget.destroy()

        label = tk.Label(
            self.frame,
            text="Choisissez le niveau du bot",
            font=("Consolas", 20),
            bg=color_gray,
            fg=color_text,
        )
        label.grid(row=0, column=0, columnspan=3, sticky="we")

        facile_button = tk.Button(
            self.frame,
            text="Bot Facile",
            font=("Consolas", 20),
            bg=color_gray,
            fg=color_text,
            command=lambda: self.start_game(mode, joueur_symbole, "facile"),
        )
        facile_button.grid(row=1, column=0, columnspan=3, sticky="we")

        difficile_button = tk.Button(
            self.frame,
            text="Bot Difficile",
            font=("Consolas", 20),
            bg=color_gray,
            fg=color_text,
            command=lambda: self.start_game(mode, joueur_symbole, "difficile"),
        )
        difficile_button.grid(row=2, column=0, columnspan=3, sticky="we")

    def run(self):
        """Lance la boucle principale de l'interface graphique."""
        self.mafenetre()
        self.window.mainloop()
