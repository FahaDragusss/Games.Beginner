import random
import time

def gri(min, max_value):
    return random.randint(min, max_value)

def gro(m):
    operators = ['+', '-', '*','**']
    return random.choice(operators[0,m])

pcount = 0

while pcount < 5:
    const_1 = gri(8, 25)
    const_2 = gri(3, 15)
    op_1 = gro(3)
    
    equation = f"{const_1} {op_1} {const_2}"
    
    try:
        correct_answer = eval(equation)
    except ZeroDivisionError:
        continue
    
    start_time = time.time()
    user_answer = input(f"What is the correct answer for {equation}? ")
    end_time = time.time()

    time_taken = end_time - start_time

    try:
        user_answer = float(user_answer)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if user_answer == correct_answer:
        pcount += 1
        print(f"Correct! You took {time_taken:.2f} seconds.")
    else:
        print(f"Incorrect. The correct answer was {correct_answer}. Try again.\nYou took {time_taken:.2f} seconds.")
    
    print(f"Current score: {pcount}/5\n")

choice = input("Congratulations! You answered 5 questions correctly. Now the real challenge begins. \nWould you like to continue or quit?\nType 'C' to continue or 'Q' to quit: ").lower()

if choice == 'c':
    print("Good luck!")
    pcount = 0  
    while pcount < 10:

        const_1 = gri(6, 9)
        const_2 = gri(2, 5)
        const_3 = gri(4, 7)
        op_1 = gro(4)
        op_2 = gro(4)
        
        equation = f"{const_1} {op_1} {const_2} {op_2} {const_3}"

        try:
            correct_answer = eval(equation)
        except ZeroDivisionError:
            continue
        
        start_time = time.time()
        user_answer = input(f"What is the correct answer for {equation}? ")
        end_time = time.time()

        time_taken = end_time - start_time

        try:
            user_answer = float(user_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_answer == correct_answer:
            pcount += 1
            print(f"Correct! You took {time_taken:.2f} seconds.")
        else:
            print(f"Incorrect. The correct answer was {correct_answer}. Try again.\nYou took {time_taken:.2f} seconds.")
        
        print(f"Current score: {pcount}/10\n")
else:
    print("womp womp, I thought you were smart ;( ")
