import wikipedia
langs = wikipedia.languages()
#print(langs)
for key, value in langs.items():
    wikipedia.set_lang(key)
    try:
        ai = wikipedia.page("Artificial intelligence")
        with open('wiki/' + value + '.txt', 'w') as f:
            f.write(ai.content)
    except:
        continue
