import sys

def word_check(word):
    for each_char in word:
        if each_char == " ":
            print('Do not use space to indicate word separation.\nInstead \
                  use "-" to separate a compound word\nInput word again')
            return False
        elif not each_char.isalpha() and each_char != "-":
            print('Do not use integers or special characters.\nInput word again')
            return False
    return True


def print_dots(x):
    if x == 1:
        print(".")
    else:
        print(".")
        print_dots(x - 1)


def guess_check(guess, lives, word, guess_word_list):
    if guess == "":
        print("Please input a letter.")
        return

    if len(guess) != 1:
        print("Please input only 1 alphabet")
        return

    guess = guess.lower()

    if guess in guess_word_list:
        print('You have already guessed this letter\nPlease try a new letter')
        return

    guess_word_list.append(guess)

    if guess in word:
        print("Great guess!")
    else:
        print("Not a good guess")
        lives -= 1
        if lives != 0:
            print("You have", lives, "lives left.")

    game_end_check(lives, word)


def blankword_check(guess_word_list, word):
    blank_word = ""
    for each_char in word:
        if each_char == "-":
            blank_word += "-"
        elif each_char in guess_word_list:
            blank_word += each_char
        else:
            blank_word += "_"
    if blank_word == word:
        print("YOU WON!\nYou have guessed the word")
        print(len(word) * "x" + ">" + blank_word + "<" + len(word) * "x")
        sys.exit()
    print(blank_word)


def game_end_check(lives, word):
    if lives == 0:
        print('Good luck next time. You have', lives, 'left.\n GAME OVER!')
        print("The word you couldn't guess was", word)
        sys.exit()
    else:
        print("Going great\nYou have", lives, "lives remaining")


# Variables needed for code
guess_word_list = []

# Word and live inputs
print('Please enter a word.\nNote: If it\'s a compound word, please separate them \
using "-" and do not use any spaces.')
word = input().lower()
while not word_check(word):
    word = input().lower()

print('Please enter the number of lives.\nThe standard number of lives is 10.')
# Input Lives
while True:
    lives = input()
    if lives.isdigit():
        lives = int(lives)
        break
    else:
        print('Lives can only be a whole number.')

# Dots so that player 2 can't see the word
print_dots(100)
print('Guess the word\nHere we go!')

# Creating blank word _____ and outputting visuals
blank_word = ""
for each_char in word:
    if each_char == "-":
        blank_word += "-"
    else:
        blank_word += "_"
print(blank_word)

while True:
    guess = input()
    guess_check(guess, lives, word, guess_word_list)
    if guess not in word:
        lives -= 1
    blankword_check(guess_word_list, word)
    print_dots(3)
