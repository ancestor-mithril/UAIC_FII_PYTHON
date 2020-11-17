import errno
import json
import os
import shutil
import unittest
from collections import Counter

from WikiPageInfo.html_parser import WikiParser
from WikiPageInfo.utils import save_wiki_page_info


class RemoveDuplicatesTesting(unittest.TestCase):
    def test_html_parser(self):
        dom_string_1 = "<html><title>title</title><script>text ta</script>" \
                       "ta<body>most most ta text<img src=\"/ta\"></img><body><html>"
        wiki_parser = WikiParser()
        wiki_parser.feed(dom_string_1)
        most_common = Counter(wiki_parser.words).most_common(1)[0][0]
        self.assertEqual("title", wiki_parser.title, "titles not equal")
        self.assertEqual("most", most_common, "most common not found")
        self.assertEqual(wiki_parser.image_src, ["http://wikipedia.com/ta"], "img src not found")

    def test_save_wiki_page_info(self):
        data = {"images": [
            "http://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Destination_America_logo.svg/"
            "220px-Destination_America_logo.svg.png",
            "http://en.wikipedia.org/wiki/DA"
        ]}
        valid_data = {
            "images": [
                "http://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Destination_America_logo.svg/"
                "220px-Destination_America_logo.svg.png"
            ]
        }
        test_folder = "test_folder"
        try:
            os.makedirs(test_folder)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        save_wiki_page_info(data, test_folder)
        with open(os.path.join(test_folder, "wiki_page_info.json"), "r") as fd:
            data = json.load(fd)
            self.assertEqual(data, valid_data, "invalid image not removed")
        self.assertEqual(os.listdir(os.path.join(test_folder, 'images')), [data["images"][0].split('/')[-1]],
                         "image not saved")
        shutil.rmtree(test_folder)


if __name__ == "__main__":
    unittest.main()
