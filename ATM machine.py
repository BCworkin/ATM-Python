### ATM Machine Simulator Program ###
## Created by Bryan Chiam ##

# function for greeting and getting the program started 
def greetings():
    print("***Welcome to Our One Stop ATM Machine!***\n")
    access = input("Please press a random number to continue. ")
    while access.isalpha() : 
        print('')
        print("Invalid character typed!")
        access = input("Please try again, enter ONLY numbers!\n ")
    return True

def login():
    accNumb = int(input("Please enter your pin number below. "))
    secret = 234567
    while accNumb != secret:
        print("Invalid pin. Please try again.")
        accNumb = int(input('Enter your pin number below.'))

def fast_cash():

def transfer():

def cash_deposit():

def balance_enquiry():

def bill_payment():

def recent_transactions():


greetings()
print('')

login()

    







