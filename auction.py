from os import system, name
bids = {}
bidding_finished = False


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a highest bid of ${highest_bid}")


def clear():
    if name == 'nt':
        _ = system('cls')

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("How much you want to bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Enter yes or no: \n")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        clear()

