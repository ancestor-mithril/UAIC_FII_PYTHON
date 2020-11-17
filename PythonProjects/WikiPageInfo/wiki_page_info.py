"""C2: Wiki Page Info

Scrieți un script care va primi ca parametru un URL ( un link către o pagina wikipedia ) și va
stoca pe disk în format JSON informații relevante găsite în pagina precum titlu, cuvantul care
apare de mai multe ori, src-urile tuturor imaginilor din pagina si imaginile salvate pe disk.
"""

import sys

from WikiPageInfo.utils import get_json_data, save_wiki_page_info
from utilities import error_print, CustomError


def run():
    """
    checks if minimum argv s are set
    gets wiki url and sets target directory to "." if not provided
    gets wiki page data and saves it to a json file, and downloads all images in target directory

    :return: nothing
    """
    if len(sys.argv) < 2:
        print("Execute the program as following:\n<your-path-to-python> wiki_page_info.py <url> [<folder-to-save>]")
        exit()
    wiki_url = sys.argv[1]
    try:
        folder = sys.argv[2]
    except IndexError:
        folder = "."
    except Exception as e:
        error_print(f"Other error: {e}")
        exit("Error 2")
    try:
        data = get_json_data(wiki_url)
        save_wiki_page_info(data, folder)
    except CustomError as e:
        error_print(f"Error: {e}")
        exit("Error")
    except Exception as e:
        error_print(f"Other error: {e}")
        exit("Error 2")


if __name__ == "__main__":
    run()
