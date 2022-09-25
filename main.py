import random
from ascii_art import *
from outcome import *

tbbt()
print("""\33[3m~Best played on desktop to view ASCII art~\33[0m
Are you up for a game of the classic \33[31m[R]ock\33[0m-\33[33m[P]aper\33[0m-\33[35m[Sc]issors\33[0m-\33[32m[L]izard\33[0m-\33[34m[Sp]ock\33[0m?\n""")

user_choice = input("Ready?\n").lower().capitalize()

print("\n\33[31mRock\33[0m-\33[33mPaper\33[0m-\33[35mScissors\33[0m-\33[32mLizard\33[0m-\33[34mSpock\33[0m!")

RPScLSp = ['R', 'P', 'Sc', 'L', 'Sp']

# Rock
if user_choice == 'R':
    print("\nYou chose \33[31mRock\33[0m!")
    rock()
    vs()
    computer_choice = random.choice(RPScLSp)
    if computer_choice == 'R':
        rock()
        print("\nComputer chose \33[31mRock\33[0m!")
        draw()
    elif computer_choice == 'Sc':
        scissors()
        print("\nComputer chose \33[35mScissors\33[0m!")
        win()
        r_sc()
    elif computer_choice == 'L':
        lizard()
        print("\nComputer chose \33[32mLizard\33[0m!")
        win()
        r_l()
    elif computer_choice == 'P':
        paper()
        print("\nComputer chose \33[33mPaper\33[0m!")
        lose()
        p_r()
    elif computer_choice == 'Sp':
        spock()
        print("\nComputer chose \33[34mSpock\33[0m!")
        lose()
        sp_r()

# Paper
elif user_choice == 'P':
    print("\nYou chose \33[33mPaper\33[0m!")
    paper()
    vs()
    computer_choice = random.choice(RPScLSp)
    if computer_choice == 'R':
        rock()
        print("\nComputer chose \33[31mRock\33[0m!")
        win()
        p_r()
    elif computer_choice == 'Sc':
        scissors()
        print("\nComputer chose \33[35mScissors\33[0m!")
        lose()
        sc_p()
    elif computer_choice == 'L':
        lizard()
        print("\nComputer chose \33[32mLizard\33[0m!")
        lose()
        l_p()
    elif computer_choice == 'P':
        paper()
        print("\nComputer chose \33[33mPaper\33[0m!")
        draw()
    elif computer_choice == 'Sp':
        spock()
        print("\nComputer chose \33[34mSpock!\33[0m")
        win()
        p_sp()

# Scissors
elif user_choice == 'Sc':
    print("\nYou chose \33[35mScissors\33[0m!")
    scissors()
    vs()
    computer_choice = random.choice(RPScLSp)
    if computer_choice == 'R':
        rock()
        print("\nComputer chose \33[31mRock\33[0m!")
        lose()
        r_sc()
    elif computer_choice == 'Sc':
        scissors()
        print("\nComputer chose \33[35mScissors\33[0m!")
        draw()
    elif computer_choice == 'L':
        lizard()
        print("\nComputer chose \33[32mLizard\33[0m!")
        win()
        sc_l()
    elif computer_choice == 'P':
        paper()
        print("\nComputer chose \33[33mPaper\33[0m!")
        win()
        sc_p()
    elif computer_choice == 'Sp':
        spock()
        print("\nComputer chose \33[34mSpock\33[0m!")
        lose()
        sp_sc()

# Lizard
elif user_choice == 'L':
    print("\nYou chose \33[32mLizard\33[0m!")
    lizard()
    vs()
    computer_choice = random.choice(RPScLSp)
    if computer_choice == 'R':
        rock()
        print("\nComputer chose \33[31mRock\33[0m!")
        lose()
        r_l()
    elif computer_choice == 'Sc':
        scissors()
        print("\nComputer chose \33[35mScissors\33[0m!")
        lose()
        sc_l()
    elif computer_choice == 'L':
        lizard()
        print("\nComputer chose \33[32mLizard\33[0m!")
        draw()
    elif computer_choice == 'P':
        paper()
        print("\nComputer chose \33[33mPaper\33[0m!")
        win()
        l_p()
    elif computer_choice == 'Sp':
        spock()
        print("\nComputer chose \33[34mSpock\33[0m!")
        win()
        l_sp()

# Spock
elif user_choice == 'Sp':
    print("\nYou chose \33[34mSpock\33[0m!")
    spock()
    vs()
    computer_choice = random.choice(RPScLSp)
    if computer_choice == 'R':
        rock()
        print("\nComputer chose \33[31mRock\33[0m!")
        win()
        sp_r()
    elif computer_choice == 'Sc':
        scissors()
        print("\nComputer chose \33[35mScissors\33[0m!")
        win()
        sp_sc()
    elif computer_choice == 'L':
        lizard()
        print("\nComputer chose \33[32mLizard\33[0m!")
        lose()
        l_sp()
    elif computer_choice == 'P':
        paper()
        print("\nComputer chose \33[33mPaper\33[0m!")
        lose()
        p_sp()
    elif computer_choice == 'Sp':
        spock()
        print("\nComputer chose \33[34mSpock\33[0m!")
        draw()

else:
    print("\n[Invalid input. Please rerun.]")