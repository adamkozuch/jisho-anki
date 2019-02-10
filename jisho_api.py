import json

import fire as fire
import requests
import anki_skripting
import glob
import os


class Jisho:
    def search_word(self):
        # add argument for correction
        end_result = []
        media_files = (glob.glob("*.mp3"))
        try:
            while(True):
                word = input('insert word')
                result = requests.get("http://beta.jisho.org/api/v1/search/words?keyword={}".format(word))
                parsed = json.loads(result.text)
                if parsed:
                    for i, v in enumerate(parsed['data'][0:3]):
                        first_reading = v['japanese'][0]
                        first_english_definition =v['senses'][0]['english_definitions'][0]
                        print(i, first_english_definition, first_reading)

                    choosed = input("which word to add (default 0) ") or 0
                    if choosed == '-1':
                        continue
                    element = parsed['data'][int(choosed)]
                    first_reading = element['japanese'][0]
                    first_english_definition = element['senses'][0]['english_definitions'][0]
                    print(first_reading, first_english_definition)
                    cards = anki_skripting.generate_cards(first_english_definition, first_reading['word'], first_reading['reading'])
                    end_result = end_result + cards
                else:
                    print('Word {0} not found'.format(word))
        except KeyboardInterrupt:
            print("Adding words to deck")
            anki_skripting.insert_cards_to_deck(end_result, media_files)




if __name__ == '__main__':
    fire.Fire(Jisho)
