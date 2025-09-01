import random
from game_data import data
from art import logo, vs

score = 0
game_over = False
account_b = random.choice(data)

def format_data(account):
    """format the account data in printables"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take the users guess and the follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)

while not game_over:
    account_a = account_b
    account_b = random.choice(data)
    if account_b == account_a:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has mre followers? Type 'A' or 'B': ").lower()

    print("\n" *20)
    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
