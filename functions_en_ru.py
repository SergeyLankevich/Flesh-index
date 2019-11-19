import textblob as tb


def lang_inp():
    language = input('Choose language:\n1. English\n2. Russian\n')
    while True:
        if (language.lower() == 'english' or language.lower() == 'en' or language == '1' or language == '1.' or
                language.lower() == '1. english'):
            language = 1
            break
        elif (language.lower() == 'russian' or language.lower() == 'ru' or language == '2' or language == '2.' or
                language.lower() == '2. russian'):
            language = 2
            break
        else:
            language = input('Choose language from the proposed:\n1. English\n2. Russian\n')
    return language


def func_en(text, lang):
    if lang == 1:
        import local_en as loc
    elif lang == 2:
        import local_ru as loc

    # Syllable count
    vowels_en = list('aeiouy')
    syllable_count = 1 if text[0] in vowels_en else 0
    for i in range(1, len(text)):
        if (text[i].lower() in vowels_en or
                (text[i] in 'lmn' and text[i + 1].lower() not in vowels_en and text[i - 1].lower() not in vowels_en)):
            syllable_count += 1

    # Sentence count
    sentence_count = 0
    for i in range(len(text) - 1):
        if text[i + 1] in '.!?' and text[i] not in '.!?':
            sentence_count += 1

    # Word count
    words = text.split()
    word_count = len(words)

    # Flesh index
    ASL = word_count / sentence_count
    ASW = syllable_count / word_count
    FRE = 206.835 - 1.015 * ASL - 84.6 * ASW

    # Text complexity
    if FRE >= 90:
        complexity = loc.COMPLEXITY_VERY_EASY
    elif FRE >= 65:
        complexity = loc.COMPLEXITY_EASY
    elif FRE >= 30:
        complexity = loc.COMPLEXITY_HARD
    else:
        complexity = loc.COMPLEXITY_VERY_HARD

    # Text objectivity
    b = tb.TextBlob(text)
    objectivity = str(((1 - b.sentiment.subjectivity)*100)) + '%'

    # Tonality of the text
    if b.sentiment.polarity >= 0.5:
        tonality = loc.POLATITY_POZITIVE
    elif b.sentiment.polarity > -0.5:
        tonality = loc.POLARITY_NEUTRAL
    else:
        tonality = loc.POLARITY_NEGATIVE

    # Response
    response = {'sentence_count': sentence_count,
                'word_count': word_count,
                'syllable_count': syllable_count,
                'FRE': FRE,
                'ASL': ASL,
                'ASW': ASW,
                'complexity': complexity,
                'objectivity': objectivity,
                'tonality': tonality,
    }
    return response


def func_ru(text, lang):
    if lang == 1:
        import local_en as loc
    elif lang == 2:
        import local_ru as loc

    # Syllable count
    vowels_ru = list('аеёиоуыэюя')
    syllable_count = 0
    for c in text:
        if c.lower() in vowels_ru:
            syllable_count += 1

    # Sentence count
    sentence_count = 0
    for i in range(len(text) - 1):
        if text[i + 1] in '.!?' and text[i] not in '.!?':
            sentence_count += 1

    # Word count
    words = text.split()
    word_count = len(words)

    # Flesh index
    ASL = word_count / sentence_count
    ASW = syllable_count / word_count
    FRE = 206.835 - 1.3 * ASL - 60.1 * ASW

    # Text complexity
    if FRE >= 90:
        complexity = loc.COMPLEXITY_VERY_EASY
    elif FRE >= 65:
        complexity = loc.COMPLEXITY_EASY
    elif FRE >= 30:
        complexity = loc.COMPLEXITY_HARD
    else:
        complexity = loc.COMPLEXITY_VERY_HARD

    # Response
    response = {'sentence_count': sentence_count,
                'word_count': word_count,
                'syllable_count': syllable_count,
                'FRE': FRE,
                'ASL': ASL,
                'ASW': ASW,
                'complexity': complexity,
                }
    return response