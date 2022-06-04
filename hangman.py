"""
Hangman - A simple hangman game made in Python 3 based on animal names
Contributors: @Neamur (ItsyBitsy)
              @savioxavier (Savio Xavier)

Still prone to bugs, proceed with caution
"""

from colors import *
import os
import random
import string
import sys

# flake8: noqa: E501 E203
# pylint: disable=invalid-name, consider-using-with

animals_list = [line.strip() for line in open("animals.txt", "r", encoding="utf-8")]

random_animal = animals_list[random.randrange(len(animals_list))]

temp = []

wrong_guesses = 0

animal_name_len = len(random_animal)

dash = "".join("_" for _ in range(animal_name_len))

hangman_stages = [
    open(f"assets/{file}", "r", encoding="utf-8").read()
    for file in os.listdir("assets/")
    if file.endswith(".txt")
]

allowed_guesses = string.ascii_letters

print(
    f"{MAGENTA}{BOLD}The word is a {animal_name_len} letter word, and is the name of an animal{RESET}"
)


while True:
    print(dash)

    for i in range(len(random_animal)):
        guess = input(f"{CYAN}Guess a letter: {RESET}")

        if guess not in allowed_guesses:
            print(f"{RED}'{guess}' is not a valid letter. Please try again.{RESET}")
            continue

        if guess.lower() in random_animal:
            ind = random_animal.index(guess)

            if random_animal.count(guess) == 1:
                dash = dash[:ind] + random_animal[ind] + dash[ind + 1 :]

                print(dash)

            if random_animal.count(guess) > 1:
                temp.extend(
                    i for i in range(len(random_animal)) if random_animal[i] == guess
                )

                for j in temp:
                    if temp[0] == 0:
                        dash = dash.replace(dash[0], guess, 1)

                    dash = dash[:j] + random_animal[ind] + dash[j + 1 :]

                temp.clear()

                print(dash)

        if dash == random_animal:
            sys.exit(f"{GREEN}{BOLD}Whatever, you win.{RESET}")

        if guess not in random_animal:
            print(f"{RED}Whooops, that's not right. Try again.{RESET}")
            print(hangman_stages[wrong_guesses + 1])

            wrong_guesses += 1

            if len(hangman_stages) == wrong_guesses + 1:
                print(f"The animal was {BLUE}'{random_animal}'{RESET}.")

                sys.exit(f"{RED}{BOLD}You are trash bruh.{RESET}")
