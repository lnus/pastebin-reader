import requests, random
from bs4 import BeautifulSoup

class PasteFetcher():
    def __init__(self):
        self.URL = "http://pastebin.com/{}"

    def getArchive(self):
        pastes = []
        plainArchive = requests.get(self.URL.format("archive")).text
        soup = BeautifulSoup(plainArchive, "html.parser")
        for td in soup.find_all("td"):
            try:
                pastes.append(td.find("a")["href"])
            except TypeError:
                pass
        return pastes    

    def pasteParser(self, pasteID = "pfcWEYiL"):
        plainPaste = requests.get(self.URL.format(pasteID)).text
        soup = BeautifulSoup(plainPaste, "html.parser")
        fullPaste = soup.find("textarea")
        parsed = fullPaste.string
        return parsed

    def randomPaste(self):
        pastes = self.getArchive()
        pastedID = random.choice(pastes)
        final = self.pasteParser(pasteID)
        return final 
