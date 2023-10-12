WORD_URL = 'http://learncodethehardway.org/words.txt'
from urllib.request import urlopen
WORDS = []

url = urlopen(WORD_URL)
print(url)
print(str(url.readline().strip(), encoding = 'utf-8'))

