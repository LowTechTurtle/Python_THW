class ParserError(Exception):
    pass

class sentence():
    def __init__(self, sub, verb, obj):
        self.sub = sub[1]
        self.verb = verb[1]
        self.obj = obj[1]

def peek(words_list):
    if words_list:
        word = words_list[0]
        return word[0]
    else:
        return None

def match(words_list, expecting):
    if words_list:
        word = words_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(words_list, word_type):
    while peek(words_list) == word_type:
        match(words_list, word_type)

def parse_verb(words_list):
    skip(words_list, 'stop')
    if peek(words_list) == 'verb':
        return match(words_list, 'verb')
    else:
        raise ParserError('Expected a verb next')

def parse_obj(words_list):
    skip(words_list, 'stop')
    if peek(words_list) == 'noun':
        return match(words_list, 'noun')
    elif peek(words_list) == 'direction':
        return match(words_list, 'direction')
    else:
        raise ParserError('Expected a noun or direction next')

def parse_sub(words_list):
    skip(words_list, 'stop')
    if peek(words_list) == 'noun':
        return match(words_list, 'noun')
    elif peek(words_list) == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError('Expected a verb next')

def parse_sentence(words_list):
    sub = parse_sub(words_list)
    verb = parse_verb(words_list)
    obj = parse_obj(words_list)
    return sentence(sub, verb, obj) 



