import csv
from datetime import datetime
from os import path

from helpers import find_user, admin_menu, buy_parts, show_parts, check_email
from models import Users


def main_menu(user):
    print('Please enter action:\n1: To view all of the parts\n2: To buys parts \n3: Logout')
    if user.role == 'admin':
        print('0: Admin menu')
    action = input()

    if action == '1':
        show_parts()
    elif action == '2':
        buy_parts(user)
    elif action == '3':
        sign_up_menu()
    elif action == '0' and user.role == 'admin':
        admin_menu(user)
    else:
        print('Not existing action')
    main_menu(user)


def register():
    while True:
        email = input('Please enter your email: ')
        if check_email(email):
            break
    user = dict()
    user['email'] = email
    user['password'] = input('Please enter your password: ')
    user['first_name'] = input('Enter first name: ')
    user['last_name'] = input('Enter last name: ')
    user['phone_number'] = input('Enter phone number: ')
    user['role'] = 'user'
    user['created'] = datetime.now()
    existing_file = path.isfile('users.csv')
    with open('users.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=user.keys())
        if not existing_file:
            writer.writeheader()
        writer.writerow(user)
    main_menu(**user)

def login_menu():
    while True:
        email = input('Please enter your email: ')
        password = input('Please enter your password: ')
        user = find_user(email, password)
        if user:
            main_menu(user)
            break
        else:
            print('Wrong email or password. Please try again.')


def sign_up_menu():
    while True:
        action = input('Please enter action:\n1: Login\n2: Register\n')
        if action == '1':
            login_menu()
            break
        elif action == '2':
            register()
            break
        else:
            print('Please enter valid action!')


if __name__ == '__main__':
    sign_up_menu()
