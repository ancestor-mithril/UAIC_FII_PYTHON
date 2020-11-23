"""C3. Spanzuratoarea

Sa se scrie o aplicatie in care utilizatorul trebuie sa ghicesca un anumit cuvant. Cuvintele vor
fi predefinite si vor avea o anumita categorie. La rulare userul alege o categorie si se va alege
un cuvant random din cele existente in categoria aleasa. Utilizatorul poate incerca cate o
litera odata. Daca ghiceste o litera, atunci i se vor afisa pozitiile din cuvant pentru litera
respectiva. Utilizatorul are voie sa greseasca literele de un anumit numar maxim de incercari
(in functie de lungimea cuvantului). In timpul jocului se va afisa numarul de incarcari ramase.
La final, se va afisa cuvantul si numarul de incercari esuate. Cuvintele vor fi salvate in fisiere
specifice categoriilor din care fac parte. De asemenea, se va tine evidenta scorurilor (tot
intr-un fisier).
"""
import os
import re

from Spanzuratoarea.utils import handle_user_input, play_game
from utilities import error_print, color_print


def run():
    game_folder = "game_folder"
    if not os.path.isdir(game_folder):
        error_print("run build_game.py script first to initialize game")
        exit(0)
    assert len(os.listdir(game_folder)) > 0, "assure there is at least 1 category ablo to be chosen"
    color_print(f"Bine ai venit la spanzuratoarea!")
    color_print(f"Alege una din urmatoarele categorii pentru joc:\n{', '.join(os.listdir(game_folder))}")
    possible_categories = "|".join(os.listdir(game_folder))
    pattern = re.compile(f"({possible_categories})", re.IGNORECASE)
    chosen_category = handle_user_input(pattern).lower()
    play_game(chosen_category, game_folder)


if __name__ == "__main__":
    run()
