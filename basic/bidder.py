from replit import clear

bids = {}
bidding_finished = False


def heighest_bidder(bidding_record):
    height_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > height_bid:
            height_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${height_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
    if should_continue == "no":
        bidding_finished = True
        heighest_bidder(bids)
    elif should_continue == "yes":
        clear()
