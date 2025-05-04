from requests import get
import xml.etree.ElementTree as et

class Dictionary:
    url = "https://api.dicionario-aberto.net"
    
    @staticmethod
    def get_word(word : str) -> str:
        return get(Dictionary.url + f"/word/{word}").json()

    @staticmethod
    def get_definitions(word : str) -> list[str]:
        try:
            data = Dictionary.get_word(word)[0]['xml']
        except Exception:
            return False
        root = et.fromstring(data)
        return root.find(".//def").text
        
