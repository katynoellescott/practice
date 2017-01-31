
def calculate_tip(bill, tip):
    return bill * (tip / 100)

def calculate_total (bill, tip):
    return bill + tip

def split_bill (bill, people):
    return bill / people

def main():
    choice = raw_input ("What would you like to do? \n 1-Calculate tip \n 2-Split the bill \n")
    if choice == "1":
        bill_input = float(raw_input("How much is your bill? $"))
        tip_input = float(raw_input("What tip percent would you like to leave? "))
        tip_total = calculate_tip (bill_input, tip_input)
        bill_total = calculate_total (bill_input, tip_total)
        print "The tip is $%.2f." % tip_total
        print "The total bill, with tip, is $%.2f." % bill_total
        split = raw_input ("Would you like to split the bill? Type y or n. ")
        if (split.upper() == "Y"):
            people_input = int(raw_input("How many people are splitting the bill? "))
            split_total = split_bill(bill_total, people_input)
            print "Each person should pay $%.2f." % split_total 
        else:
            print "Thank you."
    elif choice == "2":
        bill_total_input = float(raw_input("What is your total bill, with tip? $"))
        people_input = int(raw_input("How many people are splitting the bill? "))
        split_total = float(split_bill(bill_total_input, people_input))
        print "Each person should pay $%.2f." % split_total
    else:
        print "I don't understand your response."


if __name__ == '__main__':
    main()

