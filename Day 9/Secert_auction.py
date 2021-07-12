from secert_auction_art import logo

print(logo)

bids = {}
bidding_completed = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_completed:
    name = input("what is your name?: ")
    amount = int(input("what's your bid value: $"))
    bids[name] = amount
    choice = input("Any other bidder? Type 'yes or 'no':\n")
    if choice == "no":
        bidding_completed = True
        find_highest_bidder(bids)
