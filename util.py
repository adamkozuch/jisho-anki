import json
import os
import urllib

import genanki
import requests
from models import english_to_kanji, kanji_to_english_card, kanji_to_reading, sound_card

def return_request_session():
    request_session = requests.Session()
    request_adapter = requests.adapters.HTTPAdapter(max_retries=3)
    request_session.mount("http://", request_adapter)
    return request_session


def proces_forvo(kanji, english):
    try:
        request_session = return_request_session()
        result = request_session.get('https://apifree.forvo.com/action/word-pronunciations/format/json/word/{0}/language/ja/rate/0/id_order/rate-desc/limit/50/key/5da601d944e2a53c663f56a815a4863f/'.format(kanji))
        data = json.loads(result.text)

        if data['items']:
            best_rating = max(data['items'], key=lambda x: x['rate'])
            if best_rating['code'] == 'ja':
                urllib.request.urlretrieve(best_rating['pathmp3'], 'sound{0}.mp3'.format(english))
                return True
            else:
                print("No pronaunciation in japanese")
                return False
        else:
            print('No audio file found')
            return False
    except Exception as e:
        print(e)
        return False


def generate_cards_extended(english_meaning, kanji, reading):
    try:
        is_aodio = proces_forvo(kanji, english_meaning)

        front = genanki.Note(
            model=english_to_kanji,
            fields=[english_meaning, kanji, reading])

        reverse = genanki.Note(
            model=kanji_to_english_card,
            fields=[kanji, english_meaning, reading])


        kanji_reading = genanki.Note(
            model=kanji_to_reading,
            fields=[kanji, reading, reading[0]])
        result = []


        audio_name = 'sound{0}.mp3'.format(english_meaning)
        if is_aodio:
            pronaunciation = genanki.Note(
                model=sound_card,
                fields=['[sound:{0}]'.format(audio_name), english_meaning, reading])
            result.append(pronaunciation)
        result.append(front)
        result.append(reverse)
        result.append(kanji_reading)
        return result

    except Exception as e:
        print(e)


def generate_cards_basic(english_meaning, kanji, reading):
    try:
        is_audio = proces_forvo(kanji, english_meaning)
        audio_name = 'sound{0}.mp3'.format(english_meaning)

        front = genanki.Note(
            model=english_to_kanji,
            fields=[english_meaning, kanji, reading])

        reverse = genanki.Note(
            model=kanji_to_english_card,
            fields=[kanji + '[sound:{0}]'.format(audio_name), english_meaning, reading])

        result = []


        if is_audio:
            print(audio_name)
            pronaunciation = genanki.Note(
                model=sound_card,
                fields=['[sound:{0}]'.format(audio_name), english_meaning, reading])
            result.append(pronaunciation)
        result.append(front)
        result.append(reverse)
        return result

    except Exception as e:
        print(e)


def insert_cards_to_deck(cards, media_files):
    my_deck = genanki.Deck(
        2059400201,
        'Japanese_words')
    my_package = genanki.Package(my_deck)
    my_package.media_files = media_files
    for card in cards:
        my_deck.add_note(card)
    my_package.write_to_file('output.apkg')
    print('Package output.apkg generated')


def print_first_three_options(jisho_json):
    for i, v in enumerate(jisho_json['data'][0:3]):
        japanese_reading = v['japanese'][0]
        english_definition = get_english_definition(v)
        print(i, english_definition, japanese_reading)


def get_english_definition(element):
    arr = element['senses'][0]['english_definitions']
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