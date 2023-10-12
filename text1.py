file = open('file')
from time import sleep
for word in file:
    word = word.strip()
    sleep(0.5)
    print(word)
