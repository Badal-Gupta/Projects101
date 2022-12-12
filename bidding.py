import random
integer = str(random.randint(1,100))
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    lives = 10
else:
    lives = 5
guess = input("Make a guess: ")
while lives > 0:
    if guess > integer:
        print("Too high")
        lives -= 1
    elif guess < integer:
        print("Too low")
        lives -= 1
    else:
        print("Correct!")
        exit()
