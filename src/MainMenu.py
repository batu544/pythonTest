# Main Menu screen design for e-commerce system !!!!!
# Imports

# fixed variables

import logging


MAX_WIDTH = 80
logging.basicConfig(filename='basic.log', filemode='w', level=logging.INFO)

# Functions
def main_menu():
    pass


def static_menu():
    print('*' * MAX_WIDTH)
    print('*', '{:^76}'.format('Welcome to PRASANTA shop'), '*')
    print('*' * MAX_WIDTH)
    print()
    print('{:<40}'.format('1. Customer Menu'))
    print('{:<40}'.format('2. Order Menu'))
    print('{:<40}'.format('3. Exit'))
    print()
    print()
    print()
    print('Enter your choice: ')
    opt = input()
    return opt.strip()


def select_choice(chc):
    """
    This function is to check what is the selection has been made by user and then call the next correct function.
    :return: None
    """
    if chc == '1':
        cust_chc = cust_menu()
        cust_action(cust_chc)
    elif chc == '2':
        order_menu()
    else:
        print('Thank you for using our system')
        exit(0)


def cust_menu():
    print('1 - View customer details')
    print('2 - Edit customer details ')
    print('3 - Add new Customer details')
    print('4 - delete Customer details ')
    print('5 - Go back! ')
    print('x - Exit')
    return input('Enter your Choice:')


def order_menu():
    pass

def cust_action(cust_opt):
    """
    based on selection perform different functions
    :return:
    """
    while cust_opt in ['1' , '2' , '3', '4' , '5', 'x']:
        if cust_opt == '1':
            cust_ID = view_customer()
            sql_connection(cust_ID)
        else:
            print('Thanks for using our system')
            break

if __name__ == '__main__':
    # main_menu()
    logging.warning('Program started...,')
    while True:
        choice = static_menu()
        print(choice)
        if choice in ['1', '2', '3']:
            select_choice(choice)
            break
        else:
            print('Enter a Valid option from above list')
