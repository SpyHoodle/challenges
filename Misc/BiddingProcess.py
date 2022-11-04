current_bid = 0
bidding = True

while bidding:
    inp = input("Would you like to place a bid? (y/n): ")

    if inp.upper() == "YES" or inp.upper() == "Y":
        valid = False
        new_bid = 0

        while not valid:
            try:
                new_bid = input("How much would you like to bid for? ")

                if "£" in new_bid:
                    new_bid = new_bid.replace("£", "")

                new_bid = round(float(new_bid), 2)

                valid = True

            except ValueError:
                print("Invalid bid! The bid must be a number.")

        if new_bid > current_bid:
            current_bid = new_bid

        else:
            print("Invalid bid! You must place a higher bid.")

        print("\nCurrent bid: £" + str(current_bid))

    elif inp.upper() == "NO" or inp.upper() == "N":
        bidding = False

    else:
        print("Invalid option, please try again.\n")

print("\nEnd of bidding!")
print("Final bid: £" + str(current_bid))
