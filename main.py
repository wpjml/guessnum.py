import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

guess_number = random.randint(1,100)

print(f"Pssst, the correct answer is {guess_number}")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def game(num):
    while num > 0:
        print(f"You have {num} attempts remaining to guess the number.")
        yournum = int(input("Make a guess: "))
        if yournum == guess_number:
            num = 0
            return print(f"You got it! The answer was {guess_number}")
        elif yournum > guess_number:
            print("Too high")
            num -= 1
        elif yournum < guess_number:
            print("Too low")
            num -= 1
        if num > 0:
            print("Guess again")
    print("You've run out of guesses, you lose.")


if level == "hard":
    game(5)
elif level == "easy":
    game(10)