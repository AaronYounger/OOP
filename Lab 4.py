
# Class Customer: cid, cname, acc_no, phone, emailID, balance, credit_card=[], debit_card
# Class Card: type, card_no, cvv, expiry data, balance

## When customer class is created, credit card and debit card will be na, then customer will be prompted do you want to add a credit or debit card, then that list
## will be called, class card will then fill in that information for that list and be stored in class customer.
## Add a function where transfer of funds based off customer balance not credit card balance


import pickle

class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.phone = ""
        self.emailID = ""
        self.balance = 0.0
        self.credit_card = []
        self.debit_card = []

    def add_customer_values(self):
        self.cid = input("Enter Customer ID: ")
        self.cname = input("Enter Customer Name: ")
        self.acc_no = input("Enter Account Number: ")
        self.phone = input("Enter Phone Number: ")
        self.emailID = input("Enter Email ID: ")
        self.balance = int(input("Enter Balance: "))

    def display_customer_values(self):
        print("Customer ID: ", self.cid)
        print("Customer Name: ", self.cname)
        print("Account Number: ", self.acc_no)
        print("Phone Number: ", self.phone)
        print("Email Address: ", self.emailID)
        print("Balance: ", self.balance)

        print("Credit Card(s):")
        if not self.credit_card:
            print("  None")
        else:
            for card in self.credit_card:
                card.display_card_info()

        print("Debit Card(s):")
        if not self.debit_card:
            print("  None")
        else:
            for card in self.debit_card:
                card.display_card_info()

    def credit_to_customer(self, cr):
        self.credit_card.append(cr)

    def debit_to_customer(self, dr):
        self.debit_card.append(dr)

    def debit_from(self, debit):
        self.balance = self.balance - debit

    def credit_to(self, debit):
        self.balance = self.balance + debit

    def display_customer_balance(self):
        print("Customer Name: ", self.cname)
        print("New Customer Balance: ", self.balance)

class Card:
    def __init__(self):
        self.type = ""
        self.card_no = ""
        self.cvv = ""
        self.expiry_data = ""
        self.card_balance = ""

    def add_card_info(self):
        self.type = input("Enter Type (CC/DC only): ")
        self.card_no = input("Enter Card Number: ")
        self.cvv = int(input("Enter CVV: "))
        self.expiry_data = input("Enter Expiry Data: ")
        self.card_balance = input("Enter Balance: ")

    def display_card_info(self):
        print("Card Type: ", self.type)
        print("Card Number: ", self.card_no)
        print("Card CVV: ", self.cvv)
        print("Expiry Data: ", self.expiry_data)
        print("Card Balance: ", self.card_balance)


while True:
    print("1. Create Customer Objects")
    print("2. Create Card Objects")
    print("3. Transfer Funds Between Customer Objects")
    print("4. Assign Card Objects to Customer Objects")
    print("5. Display Customer Info")
    print("6. Display Card Info")
    print("7. Commit (Create File)")
    print("8. Exit")

    option = int(input("Select Action: "))

    if option == 1:
        c1 = Customer()
        c2 = Customer()

        c1.add_customer_values()
        c2.add_customer_values()

    elif option == 2:
        ccd1 = Card()
        ccd2 = Card()
        ccd3 = Card()
        ccd4 = Card()

        ccd1.add_card_info()
        ccd2.add_card_info()
        ccd3.add_card_info()
        ccd4.add_card_info()


    elif option == 3:
        debit = int(input("Enter Amount to be Transferred: "))
        c1.debit_from(debit)
        c2.credit_to(debit)

        c1.display_customer_balance()
        c2.display_customer_balance()

    elif option == 4:

        if ccd1.type == "CC":
            c1.credit_to_customer(ccd1)
        elif ccd1.type == "DC":
            c1.debit_to_customer(ccd1)

        if ccd2.type == "CC":
            c1.credit_to_customer(ccd2)
        elif ccd2.type == "DC":
            c1.debit_to_customer(ccd2)

        if ccd3.type == "CC":
            c1.credit_to_customer(ccd3)
        elif ccd3.type == "DC":
            c1.debit_to_customer(ccd3)

        if ccd4.type == "CC":
            c2.credit_to_customer(ccd4)
        elif ccd4.type == "DC":
            c2.debit_to_customer(ccd4)

    elif option == 5:
        c1.display_customer_values()
        c2.display_customer_values()

    elif option == 6:
        ccd1.display_card_info()
        ccd2.display_card_info()
        ccd3.display_card_info()
        ccd4.display_card_info()

    elif option == 7:
        f1 = open("Bank_Information.dat", "ab")
        pickle.dump((c1, c2, ccd1, ccd2, ccd3. ccd4), f1)

    elif option == 8:
        print("Thank You For Using Program")
        break









