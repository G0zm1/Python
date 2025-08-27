import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if c_score == u_score:
        return "It's a draw!\n"
    elif c_score == 0:
        return "Computer got an Blackjack. You lose!\n"
    elif u_score == 0:
        return "You win with a Blackjack!\n"
    elif u_score > 21:
        return "You went over. You lose!\n"
    elif c_score > 21:
        return "Computer went over. You won!\n"
    elif c_score > u_score:
        return "You lose!\n"
    else:
        return "You win!\n"

def play_game():
    print(logo)
    players_hand = []
    computers_hand = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        players_hand.append(deal_card())
        computers_hand.append(deal_card())

    while not game_over:
        user_score = calculate_score(players_hand)
        computer_score = calculate_score(computers_hand)
        print(f"\nYour cards: {players_hand}, current score: {user_score}")
        print(f"Computer's first card: {computers_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score >21:
            game_over = True
        else:
            another_card = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == "y":
                players_hand.append(deal_card())
            else:
                game_over = True


    while computer_score != 0 and computer_score < 17:
        computers_hand.append(deal_card())
        computer_score = calculate_score(computers_hand)

    print(f"\nYour final hand: {players_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computers_hand}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()
