from termcolor import colored
import random
import csv

wordlist = []
with open("sgb-words.txt") as csvfile:
    lines = csvfile.readlines()
    print(type(lines))

# https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt

word = random.choce(wordlist)
guess = input('Guess: ').lower()

color_database = {}

for x in range(len(word)):
    if word[x] == guess[x]:
        color_database.update({word[x] : 'green'})
    elif guess[x] in word:
        color_database.update({guess[x] : 'yellow'})
    else:
        color_database.update({guess[x] : 'white'})

print(color_database)

for letter in guess:
    print( "|" + colored(letter, color_database[letter]), end="" + "|")