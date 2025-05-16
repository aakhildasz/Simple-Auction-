bids = {}

continue_bidding = True

def find_highest_bidder(bid_dictionary):
    winner = ""
    highest_bid = 0

    max(bid_dictionary)

    for bidders in bid_dictionary:
        bidder_amount = bid_dictionary[bidders]

        if bidder_amount > highest_bid:
            highest_bid = bidder_amount
            winner = bidders

    print(f"The winner is {winner.upper()} with the bid amount of ${highest_bid}")


while continue_bidding:
    bidder = input("Enter your name: ")
    bid_amount = int(input("Enter the bid amount: $"))

    bids[bidder] = bid_amount

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
