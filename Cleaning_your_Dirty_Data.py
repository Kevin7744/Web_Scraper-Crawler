"""
Returns a list of 2-grams found in the wikipedia.
n-grams is a sequence of n words used in a text or speech
recurring set of words that are often used together.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter

def cleanSentence(sentence):
    # splits sentences into words
    sentence = sentence.split(' ')
    # strip punctuation and whitespace characters
    sentence = [word.strip(string.punctuation+string.whitespace)
                for word in sentence]
    # removes single word character expect 'i' and 'a'
    sentence = [word for word in sentence if len(word) > 1
                or (word.lower() == 'a' or word.lower() == 'i')]
    return sentence

def cleanInput(content):
    # removes newlines and citations
    content = re.sub('\n|[[\d+\]]', ' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    # split text into sentences based on location of periods followed by a space
    sentences = content.split('. ')

    return [cleanSentence(sentence) for sentence in sentences]

# creates n-grams
def getNgramsFromSentences(content, n):
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = Counter()
    for sentence in content:
        # list are unhashable
        newNgrams = [' '.join(ngram) 
                     for ngram in getNgramsFromSentences(sentence, 2)]
        ngrams.update(newNgrams)
    return(ngrams)

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'rw-content-text'}).get_text
ngrams = getNgrams(content, 2)
print(ngrams)
print('2-grams count is: '+str(len(ngrams)))
