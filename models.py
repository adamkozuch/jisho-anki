import genanki
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

sound_card = genanki.Model(
    160739111519,
    'sound model',
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

kanji_to_english_card = genanki.Model(
    160739118319,
    'kanji model',
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

english_to_kanji = genanki.Model(
    160739191319,
    'english model',
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

kanji_to_reading = genanki.Model(
    1607391018319,
    'kanji reading model',
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
