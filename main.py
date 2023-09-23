from termcolor import colored
import random
import csv

wordlist = []
with open("sgb-words.txt") as textfile:
  lines = textfile.readlines()
  for line in lines:
    wordlist.append(line.replace('\n', ''))

# https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt

word = random.choice(wordlist)
while True:  #inf attempts
  guess = input('Guess: ').lower()
  if len(guess) != len(word):
    print(colored(f'thats a {len(guess)} letter word dummy', 'red'))
    continue

  color_database = {}

  for x in range(len(word)):
    if word[x] == guess[x]:
      color_database.update({word[x]: 'green'})
    elif guess[x] in word:
      color_database.update({guess[x]: 'yellow'})
    else:
      color_database.update({guess[x]: 'white'})

  for x in range(len(word)):
    if guess[x] == word[x]:
      colored_output = colored(guess[x], color_database[x])
    print("|" + colored_output, end="" + "|")
  print('\n')

  if guess == word:
    print('you won')
    break
