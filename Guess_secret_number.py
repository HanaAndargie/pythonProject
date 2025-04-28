import random

def guess(x):
    rand_number = random.randint(1,x)
    guess = 0
    while guess !=rand_number:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < rand_number:
            print("Sorry, guess again. Too low.")
        elif guess > rand_number:
            print("Sorry, guess again. Too high. ")
    print(f"yay, congrats. You have guessed the number {rand_number}")

guess(10)
