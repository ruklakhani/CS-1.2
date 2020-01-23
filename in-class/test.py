from random import randint

filename = "/Users/ruklakhani/dev/courses/Term3/CS1.2/in-class/words.txt"

my_file = open(filename, "r")

lines = my_file.readlines()

random_index = randint(0, len(lines)-1)
print(lines[random_index])
