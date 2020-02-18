from random import randrange, shuffle, randint
from sys import argv, exit

filename = "test.txt"
lines = open(filename, "r").read()
words = lines.split()

my_histogram = {}


def histogram():
    for word in words: 
        if word in my_histogram:
            my_histogram[word]+= 1
        else:
            my_histogram[word]= 1
    return my_histogram 

def unique_words(rand_histogram):
    number_of_unique_words = len(rand_histogram)
    return number_of_unique_words

def frequency(word, rand_histogram): 
    frequency_of_word = rand_histogram[word]
    return frequency_of_word

def get_tokens(histogram):
    tokens = 0
    for key, value in histogram.items():
        tokens += value
    return tokens

def sample(rand_histogram):
    tokens = get_tokens(rand_histogram)
    rand_num = randint(0, tokens)
    total = 0
    for key, value in rand_histogram.items():
        total += value
        if total >= rand_num:
            return key


my_histogram = histogram()

print(sample(my_histogram))

print('Histogram contains ' + str(unique_words(my_histogram)) + ' unique words')

# print('the word fiend appears:' + str(frequency("fiend", my_histogram)))