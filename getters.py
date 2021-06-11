import csv
from os import path

from models import Users, Parts, Orders



def get_users():
    users_list = []
    if path.isfile('users.csv'):
        with open('users.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                users_list.append(Users(**row))
    return users_list


def get_parts():
    parts_list = []
    if path.isfile('parts.csv'):
        with open('parts.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                parts_list.append(Parts(**row))
    return parts_list

def get_orders():
    order_list = []
    if path.isfile('orders.csv'):
        with open('orders.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                order_list.append(Orders(**row))
    return order_list



