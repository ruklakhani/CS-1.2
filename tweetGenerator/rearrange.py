import sys 
import random

def printRandom(words):
    random.shuffle(words)
    length = len(words)
    for i in range(0, length):
        print(words[i], end=" ")

printRandom(sys.argv[1:])