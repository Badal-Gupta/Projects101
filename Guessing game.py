import random
def choice_game():
    integer = str(random.randint(1,100))
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        print("You have 10 attempts remaining to guess the number")
        lives = 10
    else:
        print("You have 5 lives")
        lives = 5

    while lives > 0:
        guess = input("Make a guess: ")
        if guess > integer:
            print("Too high")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number")
        elif guess < integer:
            print("Too low")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number")
        else:
            print("Correct, You guessed it right ")
            exit()
    print(f"You lost, The guessed number is {integer}")
switch = True
while switch:
    choice_game()
    user_want = input("Type 'y' to play that game again type 'n' to exit: ")
    if user_want =='n':
        switch = False