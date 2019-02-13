import json

import fire as fire
import requests
import anki_skripting
import glob
import os


class Jisho:
    def enter_words(self):
        end_result = []
        try:
            while(True):
                print('Type -exit to exit and generate Anki package ')
                word = input('Word to search: ')
                if word == "-exit":
                    raise KeyboardInterrupt
                s = requests.Session()
                a = requests.adapters.HTTPAdapter(max_retries=3)
                s.mount("http://", a)
                result = s.get("http://beta.jisho.org/api/v1/search/words?keyword={}".format(word))
                parsed = json.loads(result.text)
                if parsed:
                    for i, v in enumerate(parsed['data'][0:3]):
                        first_reading = v['japanese'][0]
                        first_english_definition = get_engilis_definition(v['senses'][0]['english_definitions']) #element['senses'][0]['english_definitions'][0]
                        print(i, first_english_definition, first_reading)

                    choosed = input("Which word to add (default 0) type -skip to skip ") or 0
                    if choosed == '-skip':
                        continue
                    if choosed == "-exit":
                        raise KeyboardInterrupt
                    # problem with non numberic vlues TODO
                    element = parsed['data'][int(choosed)]
                    first_reading = element['japanese'][0]
                    first_english_definition = get_engilis_definition(element['senses'][0]['english_definitions']) #element['senses'][0]['english_definitions'][0]
                    print(first_reading, first_english_definition)
                    cards = anki_skripting.generate_cards(first_english_definition, first_reading['word'], first_reading['reading'])
                    end_result = end_result + cards
                else:
                    print('Word {0} not found'.format(word))

        except KeyboardInterrupt:
            media_files = (glob.glob("*.mp3"))
            print("Adding words to deck")
            print(media_files)
            anki_skripting.insert_cards_to_deck(end_result, media_files)
            clean_up()

        except Exception as e:
            print(e)

def get_engilis_definition(arr):
    if len(arr) > 3:
        return ', '.join(arr[:3])
    else:
        return ', '.join(arr)

def clean_up():
    dir_name = os.getcwd()
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".mp3"):
            os.remove(os.path.join(dir_name, item))

if __name__ == '__main__':
    fire.Fire(Jisho)
