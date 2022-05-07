# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

from os import system, name
from art import vs, logo
from game_data import data
from random import randint


# Function to clear the screen
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def generate_data():
    """Generate the game data"""
    random_number = randint(0, len(data) - 1)
    name = data[random_number]["name"]
    followers = data[random_number]["followers"]
    return name, followers

def compare():
    """Check if a guess is correct and return the guess"""        
    if first[1] > second[1]:
        if guess == "a":
            return True

        else:
            return False

print(logo)
score = 0
second = generate_data()

end = False
while not end:
    # Extract data from game_data.py
    first = second
    second = generate_data()
    while first == second:
        second = generate_data()

    # Print the data
    print(f"A - {first[0]}")
    print(vs)
    print(f"B - {second[0]}")
    guess = input("\nWho Has More Instagram Followers? Enter A or B: ").lower()
    
    clear()
    print(logo)

    returned = compare()
    if returned == True:
        score += 1
        print("\nYou Guessed It Correctly! Your current score is {}".format(score))

    else:
        end = False
        print("You got it wrong! Your Final Score is {}".format(score))