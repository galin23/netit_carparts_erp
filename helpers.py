import csv
from os import path
from datetime import datetime

from getters import get_users, get_parts
from models import Users, Orders


def create_order(user, selected_parts, total_price, profit):
    order = dict()
    order['date'] = datetime.now()
    order['order_by'] = user.email
    order['total_price'] = total_price
    order['product_list'] = ','.join([x.name for x in selected_parts])
    order['profit'] = profit
    file_exist = path.isfile('orders.csv')
    with open('orders.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=order.keys(), delimiter=';')
        if not file_exist:
            writer.writeheader()
        writer.writerow(order)
    print('Order complete.')


def show_parts(user):
    parts = get_parts()
    print('Available parts: ')
    print('Code, Name')
    for part in parts:
        print(f'{part.code}, {part.name}')
    user_picks = input('Please select part(s) for detail information using the code (1 2 3): ').split()
    selected_parts = []
    for part in parts:
        for pick in user_picks:
            if part.code == pick:
                selected_parts.append(part)

    for part in selected_parts:
        part.print_info()
        print(20 * '-')


def buy_parts(user):
    parts = get_parts()
    print('Available parts: ')
    print('Code, Name, Price')
    for part in parts:
        print(f'{part.code}, {part.name}, {part.price_sell}')
    user_picks = input('Please select part(s) to buy using the code (1 2 3): ').split()
    selected_parts = []
    for part in parts:
        for pick in user_picks:
            if part.code == pick:
                selected_parts.append(part)

    total_price = 0
    profit = 0
    for part in selected_parts:
        part.print_info()
        total_price += part.get_price_sell()
        profit += part.get_price_sell() - part.get_price_buy()
        print(20 * '-')
    print(f'Total price: {total_price:.2f}$')
    action = input('Confirm the order (y): ')
    if action == 'y' or action == 'yes':
        create_order(user, selected_parts, total_price, profit)
    else:
        buy_parts(user)


def main_menu(user):
    print('Please enter action:\n1: To view all of the parts\n2: To buys parts \n3: Logout')
    if user.role == 'admin':
        print('0: Admin menu')
    action = input()

    if action == '1':
        show_parts(user)
    elif action == '2':
        buy_parts(user)
    elif action == '3':
        login_menu()
    elif action == '0' and user.role == 'admin':
        # admin menu
        pass
    else:
        print('Not existing action')
    main_menu(user)


def find_user(email, password):
    users = get_users()
    for user in users:
        if user.email == email and password == user.password:
            return user
    return None


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


def check_email(email):
    for user in get_users():
        if user.email == email:
            print('Email already exist. Please enter other email or contact administrator for password recovery.')
            return False
    return True


def register():
    # email = ''
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
    main_menu(Users(**user))
