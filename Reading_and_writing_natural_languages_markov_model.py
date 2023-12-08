from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum

def retrieveRandomWord(wordList):
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word
        
def buildWordDict(text):
    # remove newlines and quotes
    text = text.replace('\n', ' ')
    text = text.replace('"', '')

    # Make sure that pucntuation marks are treated as 
    # their own words so as to be included in the markov chain
    punctuation = [',', '.',';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, ' {}'.format(symbol));

    words = text.split(' ')
    # filter out empy words
    words = [words for word in words if word != '']

    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            # Create a new dictionary for this word
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[words[i-1]][words[i]]] = 0
        wordDict[words[i-1]][words[i]] += 1
        return wordDict


text = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt')
           .read(), 'utf-8')
wordDict = buildWordDict(text)

# Generate markov chain of length 100
length = 100
chain = ['I']
for i in range(0, length):
    newWord = retrieveRandomWord(wordDict[chain[-1]])
    chain.append(newWord)

print(' '.join(chain))