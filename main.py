from functions_en_ru import *

lang = lang_inp()
if lang == 1:
    import local_en as loc
elif lang == 2:
    import local_ru as loc

text = input(loc.TEXT_INPUT)
language = ''
# Correct input
while True:
    english = False
    russian = False
    for char in text:
        if char.isalpha():
            if 'a' <= char.lower() <= 'z':
                english = True
            elif 'а' <= char.lower() <= 'я':
                russian = True
            if english and russian:
                break
    else:
        language = 'english' if english else 'russian'
        break
    text = input(loc.TEXT_LANGUAGE)

# Point in the end of the text
if text[-1] not in list('.!?'):
    text = text + '.'

if language == 'english':
    response = func_en(text, lang)
else:
    response = func_ru(text, lang)
print(loc.WORDS, response['word_count'])
print(loc.SYLLABLES, response['syllable_count'])
print(loc.ASW, response['ASW'])
print(loc.ASL, response['ASL'])
print(loc.FRE, response['FRE'])
print(response['complexity'])
if language == 'english':
    print(loc.TON, response['tonality'])
    print(loc.OB, response['objectivity'])
