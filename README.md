# jisho-anki - opinionated command line for creating japanese flashcards with anki

Janki is a command line for automatic search of given word in Jisho dictionary and creating 
from it collection from which anki package can be generated. For each added word janki generated
four cards with following content:


<br>
<br>
Card with word written with kanji and english meaning on the back:
<br>
<img src='https://user-images.githubusercontent.com/5136443/53291111-6764b080-37ae-11e9-98a4-8de755b50cb3.PNG' width=270px height=200px>
<br> Card with english meaning on the front and kanji on the back. 
This type of card is integrated with kanji colorer. Hightly recomended to install this plugin.

<img src='https://user-images.githubusercontent.com/5136443/53291112-6764b080-37ae-11e9-9560-a36476ca2f05.PNG' width=270px height=200px>
<br>
Kanji on the front and reading written in hiragana on the back
<img src='https://user-images.githubusercontent.com/5136443/53291148-cb877480-37ae-11e9-8bdb-d86941a4153e.PNG' width=270px height=200px>
<br>
Audio with pronaunciation on the front and english meaning on the back. It is availible only for subscribers of forvo api.
<img src='https://user-images.githubusercontent.com/5136443/53291149-cc200b00-37ae-11e9-8fa9-24e05eea08db.PNG' width=270px height=200px>

To configure fovro for pronaunciation please
enter api key into config.py

```
FORVO_API_KEY = 'some_api_key'
```

<br>

##jisho-anki usage
```
python3 jisho_api.py search  word
```



Script enters loop where we can add multiple 
words at once. When you finished adding words
just type `-exit` . After that, package that can be imported 
to Anki will be generated in local directory.

