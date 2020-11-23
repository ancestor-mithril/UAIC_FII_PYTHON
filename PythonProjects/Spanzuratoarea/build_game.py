import errno
import os


words = {
    "sport": ["fotbal", "baschetbal", "handbal", "volei", "sah"],
    "masini": ["masina", "tir", "camion", "duba"]
}


def run(words):
    game_folder = "game_folder"
    try:
        os.makedirs(game_folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    for i in words.keys():
        with open(os.path.join(game_folder, str(i)), "w") as fd:
            fd.write(str(words[i]))


if __name__ == "__main__":
    run(words)
