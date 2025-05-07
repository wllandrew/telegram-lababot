from requests import get

class Wiki:
    def __init__(self, word):
        self.url = f"http://en.wikipedia.org/w/api.php?action=query&rvprop={word}&format=json"