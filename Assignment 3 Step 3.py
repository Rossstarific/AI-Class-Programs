import nltk
from urllib import request
from nltk.tokenize import RegexpTokenizer
import re
import string
import sys
from collections import Counter, defaultdict
import random
from operator import mul
import functools
from nltk import bigrams
from nltk.probability import FreqDist
from nltk import Text

def allPlays():
    def As_You_Like_It():
        url = "http://www.gutenberg.org/files/1786/1786.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[10672:149648]
        raw.replace('\n', ' ')
        return raw;

    def Two_Noble_Kinsman():
        url = "http://www.gutenberg.org/files/1542/1542.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[13394:160639]
        raw.replace('\n', ' ')
        return raw;

    def Comedy_Of_Errors():
        url = "http://www.gutenberg.org/files/1104/1104.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[11006:104661]
        raw.replace('\n', ' ')
        return raw;

    def Merchant_Of_Venice():
        url = "http://www.gutenberg.org/files/1779/1779.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[10889:144834]
        raw.replace('\n', ' ')
        return raw;

    def A_Midsummer_Nights_Dream():
        url = "http://www.gutenberg.org/files/1778/1778.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[10755:120599]
        raw.replace('\n', ' ')
        return raw;

    def Othello():
        url = "http://www.gutenberg.org/files/1793/1793.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[10510:187992]
        raw.replace('\n', ' ')
        return raw;

    def Romeo_And_Juliet():
        url = "http://www.gutenberg.org/files/1513/1513.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[13961:159212]
        raw.replace('\n', ' ')
        return raw;

    def Julius_Caesar():
        url = "http://www.gutenberg.org/files/1785/1785.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[11252:140870]
        raw.replace('\n', ' ')
        return raw;

    def Hamlet():
        url = "http://www.gutenberg.org/files/1787/1787.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[10785:210063]
        raw.replace('\n', ' ')
        return raw;

    def King_Lear():
        url = "http://www.gutenberg.org/files/1794/1794.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[10549:185333]
        raw.replace('\n', ' ')
        return raw;

    return Othello() + ' ' + Romeo_And_Juliet() + ' ' + Julius_Caesar() + ' ' + Hamlet() + ' ' + King_Lear() + ' ' + As_You_Like_It() + ' ' + Two_Noble_Kinsman() + ' ' + Comedy_Of_Errors() + ' ' + Merchant_Of_Venice() + ' ' + A_Midsummer_Nights_Dream();

def Tokenize(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return tokens;

allPlaysToken = Tokenize(allPlays())
playsBigrams = nltk.bigrams(allPlaysToken)

bigrams = {}
for index,word in enumerate(allPlaysToken):
    if index < len(allPlaysToken) - 1:
        w1 = allPlaysToken[index]
        w2 = allPlaysToken[index + 1]
        bigram = (w1, w2)

        if bigram in bigrams:
            bigrams[bigram] = bigrams[bigram] + 1
        else:
            bigrams[bigram] = 1

sorted_bigrams = sorted(bigrams.items(), key = lambda
                        pair:pair[1], reverse = True)

def generate_text(text, initialword, numwords):
    bigrams = list(nltk.ngrams(text, 2))
    cpd = nltk.ConditionalProbDist(nltk.ConditionalFreqDist(bigrams),
                                   nltk.MLEProbDist)
    word = initialword
    words = [initialword]
    for i in range(numwords):
        word = cpd[word].generate()
        words.append(word)
    print(' '.join(words) + '.')

generate_text(allPlaysToken, "She", 100)

