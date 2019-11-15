import textblob as tb

text = 'Wrgueraogu owrgfoaru guhOUUGy iyiyv. Vyyivq, iuuirwg, wrgrgwr. Wrgwrg. Wegwrgwrg.'
b = tb.TextBlob(text)
print()
language = 'english'
vowels_en = ''

if language == 'english':
    b = b.correct()
    ASL = 0
    ASW = 0
    FRE = 206.835 - 1.015 * ASL - 84.6 * ASW
    '''Предложений: 2
    Слов: len(zen.words)
    Слогов: slogov += 1 if x for x in 
    Средняя длина предложения в словах: 
    Средняя длина слова в слогах: 
    Индекс удобочитаемости Флеша: FRE = 206.835 - 1.015 * ASL - 84.6 * ASW
    Очень трудно читать. завитсит от FRE
    Тональность текста: нейтральный 'положительная' if b.sentiment.polarity >= 0.5 else 'нейтральная' if b.sentiment.polarity > -0.5 else 'отрицательная'
    Объективность: ((1 - b.sentiment.subjectivity)*100) %'''
else:
    b = b.correct()
    ASL = 0
    ASW = 0
    FRE = 206.835 - 1.3 * ASL - 60.1 * ASW
    '''Предложений: 8
    Слов: 
    Слогов: 49
    Средняя длина предложения в словах: 3.125
    Средняя длина слова в слогах: 1.96
    Индекс удобочитаемости Флеша: FRE = 206.835 - 1.3 * ASL - 60.1 * ASW
    Текст очень легко читается(для младших школьников).
    Тональность текста: нейтральный'''


