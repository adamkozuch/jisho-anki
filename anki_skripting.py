import time

import genanki
import json
import requests
import urllib
import os

# each card should have different color
fields = [
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'Hint'},
]
templates = [
    {
        'name': 'Card 1',
        'qfmt': '{{Question}}{{hint:Hint}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    }]
my_model = genanki.Model(
    160739111519,
    'My model1',
    fields=fields,
    templates=templates,
    css='''.card {
        font-family: honyaji-re;
        font-size: 40px;
        text-align: center;
        color: black;
        background-color: white;
        }
        .jp { font-size: 35px }
            .win .jp { font-family: "arial", "arial"; }
        .mac .jp { font-family: "honyaji-re", "ヒラギノ明朝 Pro"; }
        .linux .jp { font-family: "Kochi Mincho", "東風明朝"; }
        .mobile .jp { font-family: "Hiragino Mincho ProN"; }'''
)

my_mode2 = genanki.Model(
    160739118319,
    'My model2',
    fields=fields,
    templates=templates,
    css='''.card {
        font-family: honyaji-re;
        font-size: 40px;
        text-align: center;
        color: black;
        background-color: yellow;
        }
        .jp { font-size: 35px }
            .win .jp { font-family: "arial", "arial"; }
        .mac .jp { font-family: "honyaji-re", "ヒラギノ明朝 Pro"; }
        .linux .jp { font-family: "Kochi Mincho", "東風明朝"; }
        .mobile .jp { font-family: "Hiragino Mincho ProN"; }'''
)

my_mode3 = genanki.Model(
    160739191319,
    'My model3',
    fields=fields,
    templates=templates,
    css='''.card {
        font-family: honyaji-re;
        font-size: 40px;
        text-align: center;
        color: black;
        background-color: Aqua;
        }
        .jp { font-size: 35px }
            .win .jp { font-family: "arial", "arial"; }
        .mac .jp { font-family: "honyaji-re", "ヒラギノ明朝 Pro"; }
        .linux .jp { font-family: "Kochi Mincho", "東風明朝"; }
        .mobile .jp { font-family: "Hiragino Mincho ProN"; }'''
)

my_mode4 = genanki.Model(
    1607391018319,
    'My model4',
    fields=fields,
    templates=templates,
    css='''.card {
        font-family: honyaji-re;
        font-size: 40px;
        text-align: center;
        color: black;
        background-color: LightCyan;
        }
        .jp { font-size: 35px }
            .win .jp { font-family: "arial", "arial"; }
        .mac .jp { font-family: "honyaji-re", "ヒラギノ明朝 Pro"; }
        .linux .jp { font-family: "Kochi Mincho", "東風明朝"; }
        .mobile .jp { font-family: "Hiragino Mincho ProN"; }'''
)


def proces_forvo(kanji, english):
    try:
        result = requests.request('GET', 'https://apifree.forvo.com/action/word-pronunciations/format/json/word/{0}/language/ja/rate/0/id_order/rate-desc/limit/50/key/5da601d944e2a53c663f56a815a4863f/'.format(kanji))
        data = json.loads(result.text)
        for d in data['items']:
            print('in d', d['code'])
            if d['code'] == 'ja':
                print(d)
        #wait untill urllib finishes
        if data['items']:
            best_rating = max(data['items'], key=lambda x: x['rate'])
            print(best_rating)
            if best_rating['code'] == 'ja':
                urllib.request.urlretrieve(best_rating['pathmp3'], 'sound{0}.mp3'.format(english))
                time.sleep(2)
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


def generate_cards(english_meaning, kanji, reading):
    try:
        is_aodio = proces_forvo(kanji, english_meaning)

        front = genanki.Note(
            model=my_mode3,
            fields=[english_meaning, kanji, reading])

        reverse = genanki.Note(
            model=my_mode2,
            fields=[kanji, english_meaning, reading])


        kanji_reading = genanki.Note(
            model=my_mode4,
            fields=[kanji, reading, reading[0]])
        result = []


        audio_name = 'sound{0}.mp3'.format(english_meaning)
        if is_aodio:
            # something weird with words
            # problem with autio files
            print(audio_name)
            # my_package.media_files = [audio_name]
            pronaunciation = genanki.Note(
                model=my_model,
                fields=['[sound:{0}]'.format(audio_name), english_meaning, reading])
            result.append(pronaunciation)
        result.append(front)
        result.append(reverse)
        result.append(kanji_reading)
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

def test_add_note_with_sound():
    my_deck = genanki.Deck(
        2059400201,
        'Japanese_words')
    print(os.getcwd())
    english_meaning  = 'bag'
    audio_name = 'sound{0}.mp3'.format(english_meaning)
    my_package = genanki.Package(my_deck)
    print(audio_name)
    my_package.media_files = [audio_name]
    pronaunciation = genanki.Note(
        model=my_model,
        fields=['[sound:{0}]'.format(audio_name), english_meaning, 'some info'])
    my_deck.add_note(pronaunciation)

    my_package.write_to_file('output.apkg')
#test_add_note_with_sound()
