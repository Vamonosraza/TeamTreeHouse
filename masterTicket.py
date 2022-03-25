TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(obj):
    return (obj * TICKET_PRICE) + SERVICE_CHARGE
    



while tickets_remaining >= 1:

    print("There are {} tickets remaining tonight!".format(tickets_remaining))

    name = input("By the way, what is your name? ")

    purchased_tickets = input("How many tickets would you like to buy tonight, {} ".format(name))
    try:
        purchased_tickets = int(purchased_tickets)
        if purchased_tickets > tickets_remaining:
            raise ValueError("There are only {} remaining".format(tickets_remaining))
    except ValueError as err:
        print("{}. Please try again".format(err))
    else:    
        price = calculate_price(purchased_tickets)

        print("Your total will be ${}. This includes the $2 from the service charge. ".format(price))

        proceed = input("Would you like to continue? ")

        if proceed.lower() == "yes":
            
            print("Here are your tickets!")
            tickets_remaining -= purchased_tickets
        else:
            proceed = input("Thank you anyways , {}".format(name))

print("Sorry, tickets are all sold out!! :(")