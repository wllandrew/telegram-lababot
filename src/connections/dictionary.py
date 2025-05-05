from requests import get
import xml.etree.ElementTree as et

class Dictionary:
    """
    Classe que faz integração com a API do Dicionário Aberto.
    """

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
        definitions = root.findall(".//def")

        return [definition.text for definition in definitions]
        
