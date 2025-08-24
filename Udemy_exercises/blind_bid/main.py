from art import logo
print(logo)


def compare_bids(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

user_bids = {}
should_continue = True

while should_continue:
    name = input("Type in your name: ")
    price = int(input("What is your bid?: $ "))

    user_bids[name] = price
    another_bids = input("another bidder? yes or no? ").lower()

    if another_bids == "yes":
        print("\n" * 20)
    elif another_bids == "no":
        should_continue = False
        compare_bids(user_bids)
    else:
        print("You have to choose 'yes' or 'no'. ")

