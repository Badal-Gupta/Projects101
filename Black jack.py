logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def calculate_score(cards):
    sum1 = sum(cards)
    if sum1 == '21' and len(cards) == 2:
        return 0
    if 11 in cards and sum1 > 21:
        cards.remove(11)
        cards.append(1)
    return sum1


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif user_score == 0:
        return "User won"
    elif computer_score == 0:
        return "Computer won"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards{user_cards}current score:{user_score}")
        print(f"Computer's first card is:{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            again = input("Type 'y' if you want to draw another card Type 'n' if you don't: ")
            if again == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    blackjack()
    clear()
