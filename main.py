import random
from ascii_art import *
from outcome import *

print("Are you up for a game of the classic [R]ock-[P]aper-[Sc]issors-[L]izard-[Sp]ock?\n")

user_choice = input("Ready?\n").lower().capitalize()

tbbt()
print("Rock-Paper-Scissors-Lizard-Spock!")

RPScLSp = ['R', 'P', 'Sc', 'L', 'Sp']

# Rock
if user_choice == 'R':
    print("\nYou chose Rock!")
    rock()
    print("\nVS")
    computer_choice = random.choice(RPScLSp)
    if computer_choice == 'R':
        rock()
        print("\nComputer chose Rock!")
        draw()
    elif computer_choice == 'Sc':
        scissors()
        print("\nComputer chose Scissors!")
        win()
        r_sc()
    elif computer_choice == 'L':
        lizard()
        print("\nComputer chose Lizard!")
        win()
        r_l()
    elif computer_choice == 'P':
        paper()
        print("\nComputer chose Paper!")
        lose()
        p_r()
    elif computer_choice == 'Sp':
        spock()
        print("\nComputer chose Spock!")
        lose()
        sp_r()

# Paper
elif user_choice == 'P':
    print("\nYou chose Paper!")
    paper()
    print("\nVS")
    computer_choice = random.choice(RPScLSp)
    if computer_choice == 'R':
        rock()
        print("\nComputer chose Rock!")
        win()
        p_r()
    elif computer_choice == 'Sc':
        scissors()
        print("\nComputer chose Scissors!")
        lose()
        sc_p()
    elif computer_choice == 'L':
        lizard()
        print("\nComputer chose Lizard!")
        lose()
        l_p()
    elif computer_choice == 'P':
        paper()
        print("\nComputer chose Paper!")
        draw()
    elif computer_choice == 'Sp':
        spock()
        print("\nComputer chose Spock!")
        win()
        p_sp()

# Scissors
elif user_choice == 'Sc':
    print("\nYou chose Scissors!")
    scissors()
    print("\nVS")
    computer_choice = random.choice(RPScLSp)
    if computer_choice == 'R':
        rock()
        print("\nComputer chose Rock!")
        lose()
        r_sc()
    elif computer_choice == 'Sc':
        scissors()
        print("\nComputer chose Scissors!")
        draw()
    elif computer_choice == 'L':
        lizard()
        print("\nComputer chose Lizard!")
        win()
        sc_l()
    elif computer_choice == 'P':
        paper()
        print("\nComputer chose Paper!")
        win()
        sc_p()
    elif computer_choice == 'Sp':
        spock()
        print("\nComputer chose Spock!")
        lose()
        sp_sc()

# Lizard
elif user_choice == 'L':
    print("\nYou chose Lizard!")
    lizard()
    print("\nVS")
    computer_choice = random.choice(RPScLSp)
    if computer_choice == 'R':
        rock()
        print("\nComputer chose Rock!")
        lose()
        r_l()
    elif computer_choice == 'Sc':
        scissors()
        print("\nComputer chose Scissors!")
        lose()
        sc_l()
    elif computer_choice == 'L':
        lizard()
        print("\nComputer chose Lizard!")
        draw()
    elif computer_choice == 'P':
        paper()
        print("\nComputer chose Paper!")
        win()
        l_p()
    elif computer_choice == 'Sp':
        spock()
        print("\nComputer chose Spock!")
        win()
        l_sp()

# Spock
elif user_choice == 'Sp':
    print("\nYou chose Spock!")
    spock()
    print("\nVS")
    computer_choice = random.choice(RPScLSp)
    if computer_choice == 'R':
        rock()
        print("\nComputer chose Rock!")
        win()
        sp_r()
    elif computer_choice == 'Sc':
        scissors()
        print("\nComputer chose Scissors!")
        win()
        sp_sc()
    elif computer_choice == 'L':
        lizard()
        print("\nComputer chose Lizard!")
        lose()
        l_sp()
    elif computer_choice == 'P':
        paper()
        print("\nComputer chose Paper!")
        lose()
        p_sp()
    elif computer_choice == 'Sp':
        spock()
        print("\nComputer chose Spock!")
        draw()

else:
    print("\n[Invalid input. Please rerun.]")