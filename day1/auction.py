def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    return winner, highest_bid

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?:  ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No': \n").lower()
    if should_continue == "no":
        continue_bidding = False
        winner, highest_bid = find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)

print(f"The winner is {winner} with a bid of ${highest_bid}.")