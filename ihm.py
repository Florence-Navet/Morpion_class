import tkinter as tk
from board import Board

color_gray = "#343434"
color_blue = "#4584b6"


class IHM:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.frame = tk.Frame(self.window)
        self.label = tk.Label(self.frame, text="Choisissez votre mode de jeu", font=("Consolas", 20),
                              background=color_gray, foreground="white")
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")

    def start_game(self, mode, bot_type=None):
        """ Démarre une nouvelle partie selon le mode choisi """
        self.board = Board(self.frame, mode, bot_type)
        self.board.setup_game()
        self.adjust_window_size()

    def adjust_window_size(self):
        """ Redimensionne la fenetre selon le mode de jeu """
        self.window.geometry("600x600")
        self.centre_window()

    def centre_window(self):
        """ Centre la fenêtre sur l'écran """
        self.window.update()
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        window_x = int((screen_width / 2) - (window_width / 2))
        window_y = int((screen_height / 2) - (window_height / 2))

        self.window.geometry(
            f"{window_width}x{window_height}+{window_x}+{window_y}")

    def mafenetre(self):
        """ Crée le menu principal avec les boutons pour choisir le mode de jeu """
        label_mode_jeu = tk.Label(self.frame, text="Choisissez votre mode de jeu", font=("Consolas", 20),
                                  background=color_gray, foreground="white")
        label_mode_jeu.grid(row=0, column=0, columnspan=3, sticky="we")

        bot_button = tk.Button(self.frame, text="Jouer contre le Bot", font=("Consolas", 20),
                               background=color_gray, foreground="white", command=self.choose_bot_type)
        bot_button.grid(row=1, column=0, columnspan=3, sticky="we")

        two_players_button = tk.Button(self.frame, text="Jouer à 2 joueurs", font=("Consolas", 20),
                                       background=color_gray, foreground="white", command=lambda: self.start_game("two_players"))
        two_players_button.grid(row=2, column=0, columnspan=3, sticky="we")

        self.frame.pack()

    def choose_bot_type(self):
        """ Choix du type de bot (facile ou difficile) """
        self.frame.grid_forget()

        label_bot_choice = tk.Label(self.frame, text="Choisissez le type de Bot", font=("Consolas", 20),
                                    background=color_gray, foreground="white")
        label_bot_choice.grid(row=0, column=0, columnspan=3, sticky="we")

        easy_button = tk.Button(self.frame, text="Bot Facile", font=("Consolas", 20),
                                background=color_gray, foreground="white", command=lambda: self.start_game("bot", "facile"))
        easy_button.grid(row=1, column=0, columnspan=3, sticky="we")

        hard_button = tk.Button(self.frame, text="Bot Difficile", font=("Consolas", 20),
                                background=color_gray, foreground="white", command=lambda: self.start_game("bot", "difficile"))
        hard_button.grid(row=2, column=0, columnspan=3, sticky="we")

        self.frame.pack()

    def mainloop(self):
        """ Lancer la boucle principale de l'interface """
        self.mafenetre()
        self.window.mainloop()
