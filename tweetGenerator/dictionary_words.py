from random import randint, sample, randrange
import sys

def random_word(number):
    words = open("/usr/share/dict/words", 'r')

    words = words.read()

    words = words.split('\n')

    sentence = []

    for i in range(0,number):
        sentence.append (words[randrange(len(words))])
    print(" ".join(sentence)+".")

if __name__ == "__main__":
    random_word (int(sys.argv[1]))