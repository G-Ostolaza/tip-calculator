import sys
import subprocess
# implement pip as a subprocess: Install colorama packages
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'colorama'])

from colorama import Fore, Back, Style

# While loop to start Tip Calulator if calculator_start is set to 'y'
calculator_start = 'y' or 'yes'
while calculator_start == 'y':
    # # # Message displayed to user
    print('Welcome to your Tip calculator')

    # # Bill amount Function
    def bill_amount():  
        # # Prompt asking the user to enter their bill amount
        try:
            user_input= float(input(Back.YELLOW + 'Enter your bill amount in dollars: '))
            print(f'Your check amount is ${user_input}')
            return user_input
        # catch if input is not a number, display prompt again
        except ValueError:
            print('You did not enter a valid number, please try again')
            return bill_amount()

    # number_of_people Function (To split the bill)
    def number_of_people():
        # # prompt asking the user how many individuals will be splitting the bill
        try:
            person_count= int(input(Fore.GREEN + 'How many people to split the bill amount: '))
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
            tip= float(input(Fore.GREEN + '\nwhat tip percentage would you like to leave? 5, 10, 12 or 15 or any other amount you like?\n'))
            additional_tip_prompt= input(Fore.GREEN + '\nWould you like to leave an additional tip? Please enter y for YES and n for NO\n')
            # Conditional to check for additional tip
            if additional_tip_prompt == 'y' or additional_tip_prompt == 'yes':
                additional_tip= float(input(Fore.GREEN + '\nwhat tip percentage would you like to leave? 5, 10, 12 or 15 or any other amount you like?\n'))
                # print('this is additonal', tip + additional_tip_prompt)
                return tip + additional_tip
            elif additional_tip_prompt == 'n' or additional_tip_prompt == 'no':
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
            print(f'Total Bill: ${round((total_bill),2)}')
        else:
            if per_person_amt % 1 == 0:
                print(f'Total Bill: ${round(total_bill,2)}')
                print(f'Each person should pay: ${"{:,}".format(per_person_amt) }')
        # conditional to check if amount is float
            elif isinstance(per_person_amt, float):
                print(f'Total Bill: ${round((total_bill),2)}')
                print(f'Each person should pay: ${round((per_person_amt),2)}')
    tip_calculator()
    calculator_start= input('Would you like to calculate another bill? Choose y for YES and n for NO : ').lower()

