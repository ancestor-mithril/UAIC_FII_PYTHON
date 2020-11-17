import errno
import os
import urllib.request
from PIL import Image
import requests
import json
from collections import Counter
from WikiPageInfo.html_parser import WikiParser


def validate_url(wiki_url: str) -> (bool, str):
    """
    checks if a response is got when get(wiki_url)
    then verifies that request target is wikipedia

    :param wiki_url: url to a wikipedia page
    :return: (True, page source), if url points to Wikipedia, (False, None), otherwise
    """
    try:
        response = requests.get(wiki_url)
    except requests.ConnectionError:
        return False, None
    except Exception:
        raise
    return wiki_url.split(".")[1] == "wikipedia" or wiki_url.startswith("91.198.174.192"), response.text


def get_json_data(wiki_url: str) -> dict:
    """
    validates url
    parses dom of wiki url
    gets title and most common word and image src-s and returns them

    :param wiki_url: url to a wikipedia page
    :return: a dictionary containing {"title": page_title, "most_common_word": max(word frequency vector), "images":
                [str = src of image for image in url]
    """
    validate, source_page = validate_url(wiki_url)
    assert validate, "url is not valid"
    wiki_parser = WikiParser()
    wiki_parser.feed(source_page)
    title = wiki_parser.title
    most_common = Counter(wiki_parser.words).most_common(1)[0][0]
    images = wiki_parser.image_src
    return {
        "title": title,
        "most_common_word": most_common,
        "images": images,
    }


def save_wiki_page_info(data: dict, folder: str):
    """
    validates destination folder
    creates images folder should it not exist
    downloads each image from src, opens it with PIL.Image, if error => format not supported, file is deleted and
    removed from image src list
    lastly, json is saved

    :param data: a dictionary containing {"title": page_title, "most_common_word": max(word frequency vector),
                "images": [str = src of image for image in url]
    :param folder: target directory for data to be saved
    :return: nothing
    """
    assert os.path.isdir(folder), "target file is not folder"
    try:
        os.makedirs(os.path.join(folder, 'images'))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    for i in data["images"]:
        filename = os.path.join(folder, 'images', i.split('/')[-1])
        urllib.request.urlretrieve(i, filename=filename)
        try:
            x = Image.open(filename)
            x.close()
        except IOError:
            os.remove(filename)
            data["images"].remove(i)
        except Exception:
            raise

    with open(os.path.join(folder, "wiki_page_info.json"), "w") as fd:
        json.dump(data, fd)
