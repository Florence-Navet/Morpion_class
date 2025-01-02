import tkinter as tk
from board import Board

color_gray = "#343434"
color_blue = "#4584b6"
color_x = "#ff6347"  # Couleur pour X (rouge tomate)
color_o = "#1e90ff"  # Couleur pour O (bleu dodger)


class IHM:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.frame = tk.Frame(self.window)
        self.label = tk.Label(self.frame, text="Choisissez votre mode de jeu", font=("Consolas", 20),
                              background=color_gray, foreground="white")
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")

    def start_game(self, mode, joueur_symbole, bot_type=None):
        """Démarre une nouvelle partie selon le mode choisi"""
        bot_symbole = "O" if joueur_symbole == "X" else "X"  # Le bot joue l'autre symbole
        self.board = Board(self.frame, mode, joueur_symbole,
                           bot_symbole, bot_type)
        self.board.setup_game()

    def mafenetre(self):
        """Crée le menu principal avec les boutons pour choisir le mode de jeu"""
        label_mode_jeu = tk.Label(self.frame, text="Choisissez votre mode de jeu", font=("Consolas", 20),
                                  background=color_gray, foreground="white")
        label_mode_jeu.grid(row=0, column=0, columnspan=3, sticky="we")

        bot_button = tk.Button(self.frame, text="Jouer contre le Bot", font=("Consolas", 20),
                               background=color_gray, foreground="white", command=lambda: self.demander_symbole("bot"))
        bot_button.grid(row=1, column=0, columnspan=3, sticky="we")

        two_players_button = tk.Button(self.frame, text="Jouer à 2 joueurs", font=("Consolas", 20),
                                       background=color_gray, foreground="white", command=lambda: self.start_game("two_players", "X"))
        two_players_button.grid(row=2, column=0, columnspan=3, sticky="we")

        self.frame.pack()

    def demander_symbole(self, mode):
        """Permet au joueur de choisir son symbole (X ou O) et le type de bot"""
        for widget in self.frame.winfo_children():
            widget.grid_forget()

        self.label = tk.Label(self.frame, text="Choisissez votre symbole", font=("Consolas", 20),
                              background=color_gray, foreground="white")
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")

        # Utilisation de la couleur de fond spécifique pour X et O
        x_button = tk.Button(self.frame, text="Jouer en tant que X", font=("Consolas", 20),
                             bg=color_x, fg="white", command=lambda: self.demander_type_bot(mode, "X"))
        x_button.grid(row=1, column=0, columnspan=3, sticky="we")

        o_button = tk.Button(self.frame, text="Jouer en tant que O", font=("Consolas", 20),
                             bg=color_o, fg="white", command=lambda: self.demander_type_bot(mode, "O"))
        o_button.grid(row=2, column=0, columnspan=3, sticky="we")

    def demander_symbole(self, mode):
        """Permet au joueur de choisir son symbole (X ou O) et le type de bot"""
        for widget in self.frame.winfo_children():
            widget.grid_forget()

        self.label = tk.Label(self.frame, text="Choisissez votre symbole", font=("Consolas", 20),
                              background=color_gray, foreground="white")
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")

        # Utilisation de la couleur de fond spécifique pour X et O
        x_button = tk.Button(self.frame, text="Jouer en tant que X", font=("Consolas", 20),
                             bg=color_x, fg="white", command=lambda: self.demander_type_bot(mode, "X"))
        x_button.grid(row=1, column=0, columnspan=3, sticky="we")

        o_button = tk.Button(self.frame, text="Jouer en tant que O", font=("Consolas", 20),
                             bg=color_o, fg="white", command=lambda: self.demander_type_bot(mode, "O"))
        o_button.grid(row=2, column=0, columnspan=3, sticky="we")

    def demander_type_bot(self, mode, joueur_symbole):

    def run(self):
        """Lancer la boucle principale de l'interface"""
        self.mafenetre()
        self.window.mainloop()
