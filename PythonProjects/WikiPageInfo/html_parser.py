from html.parser import HTMLParser
import re
import string
from PIL import Image


class WikiParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = None
        self.is_title = False
        self.is_body = False
        self.is_script = False
        self.words = []
        self.word_pattern = re.compile(r"\w+")
        self.image_src = []

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        """
        sets flags if opening tags are found.
        if image, checks src, and formats them to be valid img urls

        :param tag:
        :param attrs:
        :return:
        """
        if tag == "title":
            self.is_title = True
        elif tag == "body":
            self.is_body = True
        elif tag == "script":
            self.is_script = True
        elif tag == "img":
            for name, value in attrs:
                if name == "src":
                    if value.startswith("//"):
                        value = "http:" + value
                    else:
                        value = "http://wikipedia.com" + value
                    if "?" not in value.split('/')[-1]:
                        self.image_src.append(value)

    def handle_endtag(self, tag):
        """
        removes flag for targeted tags if their end tag si found

        :param tag:
        :return:
        """
        if tag == "title":
            self.is_title = False
        elif tag == "body":
            self.is_body = False
        elif tag == "script":
            self.is_script = False

    def handle_data(self, data):
        """
        saves title only if title flag is set, and adds words only if body and not script

        :param data:
        :return:
        """
        if self.is_title:
            self.title = data
        if self.is_body and not self.is_script:
            self.words += re.findall(self.word_pattern, data)

