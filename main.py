import requests
import random
from bs4 import BeautifulSoup

class PasteFetcher():
    def __init__(self):
        self.URL = "http://pastebin.com/{}"

    def get_archive(self):
        pastes = []
        plain_archive = requests.get(self.URL.format("archive")).text
        soup = BeautifulSoup(plain_archive, "html.parser")
        for td in soup.find_all("td"):
            try:
                pastes.append(td.find("a")["href"])
            except TypeError:
                pass
        return pastes    

    def parse_paste(self, paste_id = "pfcWEYiL"):
        plain_paste = requests.get(self.URL.format(paste_id)).text
        soup = BeautifulSoup(plain_paste, "html.parser")
        full_paste = soup.find("textarea")
        parsed = full_paste.string
        return parsed

    def random_paste(self):
        pastes = self.get_archive()
        paste_id = random.choice(pastes)
        final = self.parse_paste(paste_id)
        return final 
