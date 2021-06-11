import csv
from os import path
from datetime import datetime

from matplotlib import pyplot as plt

from getters import get_users, get_parts, get_orders


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


def show_parts():
    parts = get_parts()
    print('Available parts: ')
    print('Code, Name, Application')
    for part in parts:
        print(f'{part.code}, {part.name}, {part.application}')
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
    print('Code, Name, Application, Price')
    for part in parts:
        print(f'{part.code}, {part.name}, {part.application}, {part.price_sell}')
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


def csv_users_update(users):
    with open('users.csv', 'w', newline='') as csvfile:
        fieldnames = users[0].__dict__.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for user in users:
            writer.writerow(user.__dict__)


def update_users(user):
    users = get_users()
    for u in users:
        if u.email == user.email:
            print('>', end='')
        u.print_info()
    selected_user_email = input('Select user by email: ')
    to_update_users = False
    for u in users:
        if u.email == selected_user_email:
            u.email = input('Please enter new email: ')
            u.password = input('Please new enter password: ')
            u.first_name = input('Enter new first name: ')
            u.last_name = input('Enter new last name: ')
            u.phone_number = input('Enter new phone number: ')
            u.role = input('Enter new role: ')
            to_update_users = True
            break
    else:
        print('Email was not found')
    if to_update_users:
        csv_users_update(users)
        print('User was successfully updated.')


def show_income():
    orders = get_orders()
    orders.reverse()
    # days = []
    # profit = []
    data = dict()
    counter = 0
    for order in orders:

        counter += 1
        if counter > 12:
            break
        # days.append(datetime.strptime(order.date[:10], '%Y-%m-%d').date())
        # profit.append(float(order.profit))
        order_date = order.date[:10]
        if order_date in data:
            data[order_date] += float(order.profit)
        else:
            data[order_date] = float(order.profit)
    plt.bar(data.keys(), data.values())
    plt.show()


def admin_menu(user):
    print(
        'Please enter action:\n1: To update user information\n2: Show registered users \n3: Show income for last 12 days')
    action = input()
    if action == '1':
        update_users(user)
    elif action == '2':
        pass
    elif action == '3':
        show_income()
    else:
        print('Invalid action')


def find_user(email, password):
    users = get_users()
    for user in users:
        if user.email == email and password == user.password:
            return user
    return None


def check_email(email):
    for user in get_users():
        if user.email == email:
            print('Email already exist. Please enter other email or contact administrator for password recovery.')
            return False
    return True
