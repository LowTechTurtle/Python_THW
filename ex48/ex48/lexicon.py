def scan(words_raw):
    directions = ['north', 'south', 'west', 'east', 'up', 'left', 'back', 'right']
    verbs = ['go', 'stop', 'kill', 'eat']
    stops = ['the', 'in', 'of', 'from', 'at', 'it']
    nouns = ['door', 'bear', 'princess', 'cabinet']
    words_list = []
    words = words_raw.strip().split()
    for word in words:
        try:
            number = int(word)
        except:
            pass
        else:
            tup0 = ('number', number)
            words_list.append(tup0)
            continue
        if word.lower() in directions:
            tup1 = ('direction', word)
            words_list.append(tup1)
        elif word.lower() in verbs:
            tup2 = ('verb', word)
            words_list.append(tup2)
        elif word.lower() in stops:
            tup3 = ('stop', word)
            words_list.append(tup3)
        elif word.lower() in nouns:
            tup4 = ('noun', word)
            words_list.append(tup4)
        else:
            tup5 = ('error', word)
            words_list.append(tup5)
    return words_list
