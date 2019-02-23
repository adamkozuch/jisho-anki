# Jisho_anki_extension

Plugin downloads word from jisho dictionary, 
and add it to anki package in local directory.
Afterwards if you have forvo subscription it is 
adding card with word pronunciation:
Before running the script you have to install requirements.txt.
You can run script with:
![alt text](https://user-images.githubusercontent.com/5136443/53291111-6764b080-37ae-11e9-98a4-8de755b50cb3.PNG  =250x250)
![alt text](https://user-images.githubusercontent.com/5136443/53291112-6764b080-37ae-11e9-9560-a36476ca2f05.PNG)
![alt text](https://user-images.githubusercontent.com/5136443/53291148-cb877480-37ae-11e9-8bdb-d86941a4153e.PNG)
![alt text](https://user-images.githubusercontent.com/5136443/53291149-cc200b00-37ae-11e9-8fa9-24e05eea08db.PNG)
```
python3 jisho_api.py enter_words
```

To configure fovro for pronaunciation please
enter api key into config.py

```
FORVO_API_KEY = 'some_api_key'
```

Script enters loop where we can add multiple 
words at once. When you finished adding words
just type `-exit` . After that, package that can be imported 
to Anki will be generated in local directory.

