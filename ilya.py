from functions_en_ru import *


text = input('Введите текст: ')
language = ''
# Корректность ввода
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
    text = input('Введите текст на одном языке: ')

# Точка в конце текста
if text[-1] not in list('.!?'):
    text = text + '.'

if language == 'english':
    response = func_en(text)
    print(response)

    '''
    Предложений:
    Слов:
    Слогов:
    Средняя длина предложения в словах:
    Средняя длина слова в слогах:
    Индекс удобочитаемости Флеша:
    Очень трудно читать.
    Тональность текста:
    Объективность:
    '''
else:
    response = func_ru(text)
    print(response)
    '''
    Предложений:
    Слов: 
    Слогов:
    Средняя длина предложения в словах:
    Средняя длина слова в слогах:
    Индекс удобочитаемости Флеша:
    Текст очень легко читается(для младших школьников).
    Тональность текста:
    '''



