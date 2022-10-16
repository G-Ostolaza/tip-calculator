import sys
import subprocess
# implement pip as a subprocess: Install colorama packages
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'colorama'])

from colorama import Fore, Back, Style

# While loop to start Tip Calulator if calculator set to 'y'
calculator_start = 'y'
while calculator_start == 'y':
    # # # Message displayed to user
    print('Welcome to your Tip calculator')

    # # Bill amount Function
    def bill_amount():  
        # # Prompt asking the user to enter their bill amount
        try:
            user_input= float(input(Back.YELLOW + 'Enter your bill amount in dollars: '))
            return user_input
        # catch if input is not a number, display prompt again
        except ValueError:
            print('You did not enter a valid number, please try again')
            return bill_amount()

    # number_of_people Function (To split the bill)
    def number_of_people():
        # # prompt asking the user how many individuals will be splitting the bill
        try:
            person_count= int(input(Fore.GREEN + 'How many people to split the billamount: '))
            return person_count
        # catch if input is not a number, display prompt again
        except ValueError:
            print('You did not enter a valid number of people!', Fore.RED +'please try again and enter a NUMBER!')
            return number_of_people()


    # # tip Percentage Function
    def tip_percentage():
        # prompt asking the user what percent would they like to leave as a tip
        try:
            print(Fore.RED + 'PLEASE LEAVE OFF THE PERCENT % SIGN')
            tip= float(input(Fore.GREEN + '\nwhat percentage of tip would you like to leave? 5, 10, 12 or 15 or any other amount you like?\n'))
            return tip
        # catch if input is not a number, display prompt again
        except ValueError:
            print('You did not enter a valid TIP PERCENTAGE!', 'please try again and enter a '+ Fore.RED + 'NUMBER!')
            return tip_percentage()

    # tip_percentage()
    def tip_calculator():
        # variable declarations
        bill = bill_amount()
        tip_amount = tip_percentage()
        people = number_of_people()
        tax_amount = bill * 0.10
        total_bill = (bill + tax_amount + (0.01 *tip_amount)*bill)
        per_person_amt = total_bill/people

        # conditional to check if bill is for 1 person
        # "{:,}".format() // is to format for thousands place with commas
        if people == 1:
            print(f' people Total Bill: ${"{:.2f}".format(total_bill)}')
        else:
            if per_person_amt % 1 == 0:
                print(f'Total Bill: ${ "{:,}".format(total_bill)}')
                print(f'Each person should pay: ${ "{:,}".format(per_person_amt)}')
        # conditional to check if amount is float
            elif isinstance(per_person_amt, float):
                print(f'Total Bill: ${"{:,}".format(total_bill)}')
                print(f"Each person should pay {'%.2f' % per_person_amt}")
    tip_calculator()
    calculator_start= input('Would you like to calculate another bill? Choose y for YES and n for NO : ').lower()

