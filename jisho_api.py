import json

import fire as fire
import glob

from util import return_request_session, print_first_three_options, get_english_definition, clean_up, generate_cards_basic, generate_cards_extended, insert_cards_to_deck


class Jisho:
    def enter_words(self, basic=False):
        end_result = []
        try:
            while True:
                try:
                    print('Type -exit to exit and generate Anki package ')
                    word = input('Word to search: ')
                    if word == "-exit":
                        raise KeyboardInterrupt

                    word_object = get_word_object(word)

                    if word_object:
                        print_first_three_options(word_object)

                        word_index = input("Which word to add (default 0) type -skip to skip ") or 0

                        # check if fire hs some options for these
                        if word_index == '-skip':
                            continue

                        if word_index == "-exit":
                            raise KeyboardInterrupt

                        try:
                            val = int(word_index)
                        except ValueError:
                            print("Value is not a number. Skipping.")
                            continue

                        if len(word_object['data']) == 0:
                            print('No such a word')
                            continue

                        if len(word_object['data']) < int(word_index):
                            print("Wrong index skipping :")
                            continue

                        choosen_object = word_object['data'][int(word_index)]
                        japanese_reading = choosen_object['japanese'][0]

                        english_definition = get_english_definition(choosen_object)
                        print(japanese_reading, english_definition)

                        if not basic:
                            cards = generate_cards_extended(english_definition, japanese_reading['word'], japanese_reading['reading'])
                        else:
                            cards = generate_cards_basic(english_definition, japanese_reading['word'], japanese_reading['reading'])

                        end_result = end_result + cards
                    else:
                        print('Word {0} not found'.format(word))

                except KeyboardInterrupt:
                    raise KeyboardInterrupt
                except Exception as e:
                    print("There was a problem ", e)



        except KeyboardInterrupt:
            media_files = (glob.glob("*.mp3"))
            print("Adding words to deck")
            print(media_files)
            insert_cards_to_deck(end_result, media_files)
            clean_up()

        except Exception as e:
            print(e)


def get_word_object(word):
    request_session = return_request_session()
    jisho_definition = request_session.get("http://beta.jisho.org/api/v1/search/words?keyword={}".format(word))
    return json.loads(jisho_definition.text)


if __name__ == '__main__':
    fire.Fire(Jisho)
