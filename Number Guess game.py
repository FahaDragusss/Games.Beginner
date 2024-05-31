#imports
import random
import sys

#variables
count = 0

#Code

def printdots(x):
    if x == 1:
        print('.')
    else:
        print('.')
        printdots(x-1)

print('This is the Number guessing game.\nYou have to select an upper and lower limit ,the computer\
\nwill generate a random number and you have to guess\nit in the least number of tries.')

while True:
    l_limit = input("Input the lower Limit")
    if l_limit.isdigit():
        l_limit = int(l_limit)
        printdots(1)
        print('Your lower Limit is',l_limit)
        break 
    else:
        printdots(1)
        print("The limit can only be a number")

while True:
    u_limit = input("Input the upper Limit")
    if u_limit.isdigit():
        u_limit = int(u_limit)
        printdots(1)
        print('Your lower Limit is',u_limit)
        break
    else:
        printdots(1)
        print("The limit can only be a number")

generated_number = random.randint(l_limit,u_limit)
printdots(2)

while True:
    while True:
        guess = input('Input Guess')
        if guess.isdigit():
            guess = int(guess)
            printdots(1)
            print('Your guess is',guess)
            break
        else:
            printdots(1)
            print('The guess can only be an integer(number)')
    count += 1
    if guess == generated_number:
        printdots(1)
        print('You guessed the number in',count,'guesses.\nIt was',generated_number)
        sys.exit()
    elif guess > generated_number:
        print('Your guess is high')
    elif guess < generated_number:
        print('Your guess is low')        

    while True:
        printdots(1)
        g_continue = input("Do you want to continue the game?\nType 'Y' or 'N'")
        if g_continue.isalpha():
            if g_continue.lower() == 'y':
                break
            else:
                printdots(1)
                print('Since your a looser here is the generated number',generated_number)
                sys.exit()
    print('Number of guesses',count)
