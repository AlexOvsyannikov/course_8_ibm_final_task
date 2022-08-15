import os

import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.environ['api_key']
URL = os.environ['url']


class Translator:
    """Class that translates text from english to french and back"""
    def __init__(self, iam_token, folder):
        self.iam = iam_token
        self.folder = folder
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {iam_token}"
        }

    def translate_from_english_to_french(self, text):
        body = {
            "sourceLanguageCode": 'en',
            "targetLanguageCode": 'fr',
            "texts": text,
            "folderId": self.folder,
        }
        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                 json=body,
                                 headers=self.headers
                                 )
        return response.json().get('translations', [])[0].get('text', '')

    def translate_from_french_to_english(self, text):
        body = {
            "sourceLanguageCode": 'fr',
            "targetLanguageCode": 'en',
            "texts": text,
            "folderId": self.folder,
        }
        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                 json=body,
                                 headers=self.headers
                                 )
        return response.json().get('translations', [])[0].get('text', '')


def english_to_french(english_text: str):
    """Translates text from english to french using Translator class"""
    translator = Translator(API_KEY, URL)
    french_text = translator.translate_from_english_to_french(english_text)
    return french_text


def french_to_english(french_text: str):
    """Translates text from french to english using Translator class"""
    translator = Translator(API_KEY, URL)
    english_text = translator.translate_from_french_to_english(french_text)
    return english_text

