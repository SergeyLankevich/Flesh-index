import textblob as tb


def func_en(text):
    # Количество слогов
    vowels_en = list('aeiouy')
    syllables_count = 1 if text[0] in vowels_en else 0
    for i in range(1, len(text)):
        if (text[i].lower() in vowels_en or
                (text[i] in 'lmn' and text[i + 1].lower() not in vowels_en and text[i - 1].lower() not in vowels_en)):
            syllables_count += 1

    # Количество предложений
    sentences_count = 0
    for i in range(len(text) - 1):
        if text[i + 1] in '.!?' and text[i] not in '.!?':
            sentences_count += 1

    # Количество слов
    words = text.split()
    words_count = len(words)

    # Индекс Флеша
    ASL = words_count / sentences_count
    ASW = syllables_count / words_count
    FRE = 206.835 - 1.015 * ASL - 84.6 * ASW

    # Сложность текста
    if FRE >= 90:
        complexity = 'Очень легко читается.'
    elif FRE >= 65:
        complexity = 'Легко читается.'
    elif FRE >= 30:
        complexity = 'Немного трудно читать.'
    else:
        complexity = 'Очень трудно читать.'

    # Объекстивность текста
    b = tb.TextBlob(text)
    objectivity = str(((1 - b.sentiment.subjectivity)*100)) + '%'

    # Тональность текста
    if b.sentiment.polarity >= 0.5:
        tonality = 'Позитивный'
    elif b.sentiment.polarity > -0.5:
        tonality = 'Нейтральный'
    else:
        tonality = 'Негативный'

    # Ответ
    response = {'sentences_count': sentences_count,
                'words_count': words_count,
                'syllables_count': syllables_count,
                'FRE': FRE,
                'ASL': ASL,
                'ASW': ASW,
                'complexity':complexity,
                'objectivity': objectivity,
                'tonality': tonality,
    }
    return response


def func_ru(text):
    # Количество слогов
    vowels_ru = list('аеёиоуыэюя')
    syllables_count = 0
    for c in text:
        if c.lower() in vowels_ru:
            syllables_count += 1

    # Количество предложений
    sentences_count = 0
    for i in range(len(text) - 1):
        if text[i + 1] in '.!?' and text[i] not in '.!?':
            sentences_count += 1

    # Количество слов
    words = text.split()
    words_count = len(words)

    # Индекс Флеша
    ASL = words_count / sentences_count
    ASW = syllables_count / words_count
    FRE = 206.835 - 1.3 * ASL - 60.1 * ASW

    # Сложность текста
    if FRE >= 90:
        complexity = 'Очень легко читается.'
    elif FRE >= 65:
        complexity = 'Легко читается.'
    elif FRE >= 30:
        complexity = 'Немного трудно читать.'
    else:
        complexity = 'Очень трудно читать.'

    # Тональность текста
    x = True
    if x:
        tonality = 'Позитивный'
    elif x:
        tonality = 'Нейтральный'
    else:
        tonality = 'Негативный'

    # Ответ
    response = {'sentences_count': sentences_count,
                'words_count': words_count,
                'syllables_count': syllables_count,
                'FRE': FRE,
                'ASL': ASL,
                'ASW': ASW,
                'complexity': complexity,
                'tonality': tonality,
                }
    return response