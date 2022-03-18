# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

from art import *
from game_data import data
from random import randint

print(logo)

def generate_data():
    random_number = randint(0, len(data) - 1)
    name = data[random_number]["name"]
    followers = data[random_number]["followers"]
    return name, followers

first = generate_data()
second = generate_data()

print(f"Comapre the follower count of the following people:\n")

def compare():
    if first[1] > second[1]:
        return 1
    
    elif first[1] < second[1]:
        return 2

print(f"A: {first[0]}")
print(vs)
print(f"B: {second[0]}")

def main():
    selected = input("\nSelect A or B: ").lower()
    result = compare() 

    end = False
    while not end:
        if selected == "a" and result == 1:
            print("Correct!")
            returned = first
            return returned

        elif selected == "b" and result == 2:
            print("Correct!")
            returned = second
            return returned

        elif selected == "a" and result == 2:
            print("Wrong!")
            end = True

        elif selected == "b" and result == 1:
            print("Wrong!")
            end = True

        first = returned

        second = generate_data()
        compare()

main()