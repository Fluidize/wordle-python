from termcolor import colored
import random

wordlist = []
with open("sgb-words.txt") as textfile:
  lines = textfile.readlines()
  for line in lines:
    wordlist.append(line.replace('\n', ''))

# https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt

word = random.choice(wordlist)
attempts = 0
while True:  #inf attempts
  guess = input('Guess: ').lower()
  if len(guess) != len(word):
    print(colored(f'thats a {len(guess)} letter word dummy', 'red'))
    continue

  for x in range(len(word)):
    if guess[x] == word[x]:
      color = 'green'
    elif guess[x] in word:
      color = 'yellow'
    else:
      color = 'white'

    print("|" + colored(guess[x], color) + "|", end="")
  print('\n')

  if guess == word:
    print(f"You spelled the word '{word}' after {attempts} attempts.")
    break

  attempts += 1
