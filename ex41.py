import random
from urllib.request import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
PHRASES = {
        "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and ***params.",
        "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
        "*** = %%%()":
        "Set *** to an instance of class %%%.",
        "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
        "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}
###
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#print(PHRASE_FIRST)

#print(sys.argv)
##sys.argv will return you a list of argument variable 
###

#for word in urlopen(WORD_URL).readlines():
#    WORDS.append(str(word.strip(), encoding = 'utf-8'))

## an alternative way for the above code
url = urlopen(WORD_URL)
while True:
    x = str(url.readline().strip(), encoding = 'utf-8')
    if x:
        WORDS.append(x)
    else:
        break

#urlopen(WORD_URL).readlines() will return a massive list with element in utf-8 encoding
#so we got str() function to help us with it
#print(WORDS)

#x = urlopen(WORD_URL)
#print(x.readlines())

###

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
#getting a list of random word from WORDS list, the number of word in that list is equivalent to the number of %%% in the snippet, which the number of class_name

    other_names = random.sample(WORDS, snippet.count("***"))
#getting a list of words for variable and method/function name
    results = []
    param_names  = []

    for i in range(0, snippet.count('@@@')):
        param_count = random.randint(1, 3)
#get a random number of parameter that the method will take
        param_names.append(', '.join( random.sample(WORDS, param_count)))
#append the random word to the param_names, the number of words equivalent to the number randomed previously
    for sentence in snippet, phrase:
#for sentence in snippet, phrase will first do sentence = snippet, after doing that and run all the block below, sentence will be phrase and run the code below again in a single loop
#        print('I dont quite understand this part')
#        print(f'sentence is {sentence}')
        result = sentence
#       result = sentence[:]

#result = sentence[:] is a python way to repicate a list, however, this sentence variable is just a string, so result = sentence[:] is just gonna replicate the string
#so we can just simply assgin the variable the normal way
        print(f'result is {result}')
        for word in class_names:
            result = result.replace('%%%', word, 1)
#replace the %%% one by one from the list class_names created earlier
        for word in other_names:
           result = result.replace("***", word, 1)
        for word in param_names:
            result = result.replace("@@@", word, 1)
        results.append(result)
#after the first assgin, the list results only got 1 element, which is the question later, then after the second assgin, the list results got 2 element
#so later we can assgin 2 var question, answer = convert(snippet, phrase)
    return results


try:
    while True:
#        snippets = list(PHRASES.keys())
        snippets = list(PHRASES)
#PHRASES.key() will return a list object, using list will turn it into a list
#alternatively, we can just use list(PHRASES)
        random.shuffle(snippets)
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            print(question)
            input("< ")
#this will make we read the question first, then press enter and we will get the answer
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
#if we hit ctrl-D then we gonna get EOFError, this is just a fancy way to quit the script without having error prompted
#we got the EOFError because the input didnt get any data and it hit the end-of-file condintion
