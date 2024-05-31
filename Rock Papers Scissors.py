#import

import sys
import random

#functions

def printdots(x):
    if x == 1:
        print('.')
    else:
        print('.')
        printdots(x-1)

#variables

actions = ['rock','papers','scissors']


#code
while True:
    print('Rock, papers or scissors')
    while True:
        choice = input()
        if choice.isalpha():
            choice = choice.lower()
            if choice == 'rock':
                break
            elif choice == 'scissors':
                break
            elif choice == 'papers':
                break
            else:
                print('Please input ROCK! , PAPERS! or SCISSORS!')

    comp_choice = actions[random.randint(0,2)]

    if comp_choice == choice:
        print('Its a tie, imagine not winning against a computer.\n\
            Wanna continue?')
        while True:
            printdots(1)
            g_continue = input("Do you want to continue the game?\nType 'Y' or 'N'")
            if g_continue.isalpha():
                if g_continue.lower() == 'y':
                    break
                else:
                    printdots(1)
                    print('Meet you next time')
                    sys.exit()

    if choice == 'rock':
        if comp_choice == 'scissors':
            print('You win, surprising')
            print('The computer choose' + comp_choice)
            while True:
                printdots(1)
                g_continue = input("Do you want to continue the game?\nType 'Y' or 'N'")
                if g_continue.isalpha():
                    if g_continue.lower() == 'y':
                        break
                    else:
                        printdots(1)
                        print('Meet you next time')
                        sys.exit()
        elif comp_choice == 'papers':
            print('You loose , LMFAO lost to a computer')
            print('The computer choose' + comp_choice)
            while True:
                printdots(1)
                g_continue = input("Do you want to continue the game?\nType 'Y' or 'N'")
                if g_continue.isalpha():
                    if g_continue.lower() == 'y':
                        break
                    else:
                        printdots(1)
                        print('Meet you next time')
                        sys.exit()

    if choice == 'papers':
        if comp_choice == 'rock':
            print('You win, surprising')
            print('The computer choose' + comp_choice)
            while True:
                printdots(1)
                g_continue = input("Do you want to continue the game?\nType 'Y' or 'N'")
                if g_continue.isalpha():
                    if g_continue.lower() == 'y':
                        break
                    else:
                        printdots(1)
                        print('Meet you next time')
                        sys.exit()
        elif comp_choice == 'scissors':
            print('You loose , LMFAO lost to a computer')
            print('The computer choose' + comp_choice)
            while True:
                printdots(1)
                g_continue = input("Do you want to continue the game?\nType 'Y' or 'N'")
                if g_continue.isalpha():
                    if g_continue.lower() == 'y':
                        break
                    else:
                        printdots(1)
                        print('Meet you next time')
                        sys.exit()

    if choice == 'scissors':
        if comp_choice == 'rock':
            print('You loose , LMFAO lost to a computer')
            print('The computer choose' + comp_choice)
            while True:
                printdots(1)
                g_continue = input("Do you want to continue the game?\nType 'Y' or 'N'")
                if g_continue.isalpha():
                    if g_continue.lower() == 'y':
                        break
                    else:
                        printdots(1)
                        print('Meet you next time')
                        sys.exit()
        elif comp_choice == 'papers':
            print('You win, surprising')
            print('The computer choose' + comp_choice)
            while True:
                printdots(1)
                g_continue = input("Do you want to continue the game?\nType 'Y' or 'N'")
                if g_continue.isalpha():
                    if g_continue.lower() == 'y':
                        break
                    else:
                        printdots(1)
                        print('Meet you next time')
                        sys.exit()


            






