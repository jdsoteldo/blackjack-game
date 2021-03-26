import random
from logo import logo
import os

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over\n"

    elif user_score == computer_score:
        return 'Draw\n'

    elif user_score == 0:
        return 'Blackjack, you win\n'

    elif computer_score == 0:
        return 'computer has blackjack, you lose.\n'

    elif user_score > 21:
        return 'you went over. you lose\n'

    elif computer_score > 21:
        return 'computer went over. you win\n'

    elif user_score > computer_score:
        return 'you win\n'

    elif computer_score > user_score:
        return 'computer wins\n'

def play():
    computer_cards =  []
    user_cards = []
    keep_play = True

    print(logo)

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    user_score = calculate(user_cards)
    computer_score = calculate(computer_cards)

    while keep_play:
        user_score = calculate(user_cards)
        computer_score = calculate(computer_cards)

        print(f"your cards: {user_cards}, your score: {user_score}")

        print(f"computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            keep_play = False

        else:
            print("Type 'y' to get a new card or 'n' to pass.\n")
            another = input()

            if another[0].lower() == 'y':
                user_cards.append(deal_cards())

            else:
                keep_play = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate(computer_cards)

    print(f"final hand: {user_cards}, final score: {user_score}")

    print(f"computer hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))


while input("Type 'y' to play or 'n' to quit\n") == 'y':
    os.system("clear")
    play()
