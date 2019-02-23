import json

import config
import fire as fire
import glob

from util import return_request_session, print_first_three_options, get_english_definition, clean_up, generate_cards_basic, generate_cards_extended, insert_cards_to_deck, save_to_words_json, proces_forvo


class Jisho:

    def list(self):
        with open('words.json') as file:
            words = json.load(file)['data']
            for w in words:
                print(w['english'], ' --- ', w['kanji'])

    def prune(self):
        with open('words.json', 'w') as file:
            json.dump({'data':[]}, file)
            clean_up()

    def generate(self):
        with open('words.json') as file:
            elements = json.load(file)['data']
            cards = []
            for obj in elements:
                cards = cards +  generate_cards_extended(obj['english'], obj['kanji'], obj['reading'])
                media_files = (glob.glob("*.mp3"))
            insert_cards_to_deck(cards, media_files)

    def search(self, basic=False, sound=True):
        try:
            word = input('Type word you want to find: ')
            word_object = get_word_object(word)

            if word_object:
                print_first_three_options(word_object)

                if len(word_object['data']) == 0:
                    raise Exception('No such a word')

                word_index = input("Which word to add (default 0) type") or 0

                try:
                    val = int(word_index)
                except ValueError:
                    raise Exception("Chosen value is not a number")


                if len(word_object['data']) < int(word_index):
                    print("Wrong index skipping :")

                choosen_object = word_object['data'][int(word_index)]
                japanese_info = choosen_object['japanese'][0]

                english_definition = get_english_definition(choosen_object)
                if config.FORVO_API_KEY:
                    proces_forvo(japanese_info['word'], english_definition)
                print(japanese_info, english_definition)
                obj = {'english': english_definition, 'kanji': japanese_info['word'], 'reading': japanese_info['reading']}
            else:
                print('Word {0} not found'.format(word))

            save_to_words_json(obj)
        except Exception as e:
            print(e)

    # def enter_words(self, basic=False, interactive=False):
    #     end_result = []
    #     objects = []
    #     try:
    #         while True:
    #             try:
    #                 print('Type -exit to exit and generate Anki package ')
    #                 word = input('Word to search: ')
    #                 if word == "-exit":
    #                     raise KeyboardInterrupt
    #
    #                 word_object = get_word_object(word)
    #
    #                 if word_object:
    #                     print_first_three_options(word_object)
    #
    #                     word_index = input("Which word to add (default 0) type -skip to skip ") or 0
    #
    #                     # check if fire hs some options for these
    #                     if word_index == '-skip':
    #                         continue
    #
    #                     if word_index == "-exit":
    #                         raise KeyboardInterrupt
    #
    #                     try:
    #                         val = int(word_index)
    #                     except ValueError:
    #                         print("Value is not a number. Skipping.")
    #                         continue
    #
    #                     if len(word_object['data']) == 0:
    #                         print('No such a word')
    #                         continue
    #
    #                     if len(word_object['data']) < int(word_index):
    #                         print("Wrong index skipping :")
    #                         continue
    #
    #                     choosen_object = word_object['data'][int(word_index)]
    #                     japanese_info = choosen_object['japanese'][0]
    #
    #                     english_definition = get_english_definition(choosen_object)
    #                     print(japanese_info, english_definition)
    #                     obj = {'english': english_definition, 'kanji': japanese_info['word'], 'reading': japanese_info['reading']}
    #                     objects.append(obj)
    #
    #
    #                     if not basic:
    #                         cards = generate_cards_extended(english_definition, japanese_info['word'], japanese_info['reading'])
    #                     else:
    #                         cards = generate_cards_basic(english_definition, japanese_info['word'], japanese_info['reading'])
    #
    #                     end_result = end_result + cards
    #                 else:
    #                     print('Word {0} not found'.format(word))
    #
    #             except KeyboardInterrupt:
    #                 raise KeyboardInterrupt
    #             except Exception as e:
    #                 print("There was a problem ", e)
    #
    #     except KeyboardInterrupt:
    #         save_to_words_json(objects)
    #         clean_up()
    #
    #     except Exception as e:
    #         save_to_words_json(objects)
    #         print(e)


def get_word_object(word):
    request_session = return_request_session()
    jisho_definition = request_session.get("http://beta.jisho.org/api/v1/search/words?keyword={}".format(word))
    result = json.loads(jisho_definition.text)
    print(result)
    return result


if __name__ == '__main__':
    fire.Fire(Jisho)
