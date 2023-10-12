def break_word(foo):
    words = foo.split(' ')
    return words

def sort_words(foo):
    """ sort the words """
    return sorted(foo)

def print_first_word(foo):
    fooo=foo.pop(0)
    print(foo)

def print_last_word(foo):
    fooo=foo.pop()
    print(foo)

def sort_sentence(dick):
    smoldick=break_word(dick)
    return sort_words(dick)

def print_first_and_last(sentence):
    first = sentence.pop(0)
    last = sentence.pop()
    print(f'The first word in the sentence is {first} and the last word in the sentence is {last}')

def print_first_and_last_sorted(foo):
    dick=sort_sentence(foo)
    print_first_word(dick)
    print_last_word(dick)




    
