# Jisho_anki_extension

Plugin downloads word from jisho dictionary, 
and add it to anki package in local directory.
Afterwards if you have forvo subscription it is 
adding card with word pronunciation:
You can run script with:
```
python3 jisho_api.py enter_words
```
Script enters loop where we can add multiple 
words at once. When you finished adding words
just type `-exit`
To configure fovro for pronaunciation please
enter api key into config.py
```
FORVO_API_KEY = 'some_api_key'
```

After adding few words just import generated package.
For now, there is just option to import notes to deck 
called Japanese_words.
