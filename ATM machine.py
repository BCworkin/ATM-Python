### ATM Machine Simulator Program ###
## Created by Bryan Chiam ##

import time 

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
    print('')
    print('Fast cash')
    option1 = '1. 50'
    option2 = '2. 100'
    option3 = '3. 200'
    option4 = '4. 500'
    option5 = '5. 1000'
    option6 = '6. 2000'
    print(option1, option2, option3, option4, option5, option6, sep='\n')
    choice = int(input('Please enter choice in terms of number indicated. (1,2,3,4,5,6) '))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
        choice = input('Please enter valid choice. ')
    if choice == 1 or choice == 2:
        print('Processing cash...')
        print('')
        time.sleep(2)
        print(' ________')
        time.sleep(.5)
        print('|        |')
        time.sleep(.5)
        print('|  _  _  |')
        time.sleep(.5)
        print('| |_ | | |')
        time.sleep(.5)
        print('|  _||_| |')
        time.sleep(.5)
        print('|        |')
        time.sleep(.5)
        print('|________|')
        time.sleep(.5)
        print('')
        print('Here is your cash, have a great day ahead!')

    

def transfer():

def cash_deposit():

def balance_enquiry():

def bill_payment():

def recent_transactions():




greetings()
print('')

login()
fast_cash()
    







