import os
def find_winner(bidder_details):
    highest_bid =0
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")



bidder_data ={}
end_bidding = False
while not end_bidding:
    Name = input("Enter your name: ")
    bid=int(input("Enter your bid: "))
    bidder_data[Name]=bid
    more_bidders=input("is there any bidders? type 'yes' or 'no': ").lower()
    if more_bidders == 'no':
        end_bidding = True
        find_winner(bidder_data)
    elif more_bidders == 'yes':
        os.system('cls')