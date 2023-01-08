import requests
import json

class WordDefiner:

    def get_definition(self, word):
        
        api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        r = requests.get(api_url)
        data = r.json()
        if not data:
            return None
        else:
            try:
                definition = data[0]['meanings'][0]['definitions'][0]['definition']
            except KeyError:
                definition=None
            try:
                example = data[0]['meanings'][0]['definitions'][0]['example']
            except KeyError:
                example = None
            return definition, example