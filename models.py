from datetime import datetime


class Users:

    def __init__(self, email, password, first_name, last_name, phone_number, role, created=datetime.now()):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.role = role
        self.created = created

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Parts:

    def __init__(self, code, name, category, price_buy, price_sell, application, manufacturer):
        self.code = code
        self.name = name
        self.category = category
        self.price_buy = price_buy
        self.price_sell = price_sell
        self.application = application
        self.manufacturer = manufacturer

    def get_price_sell(self):
        try:
            price = float(self.price_sell.replace(',', '.'))
            return price
        except ValueError:
            return 0

    def get_price_buy(self):
        try:
            price = float(self.price_buy.replace(',', '.'))
            return price
        except ValueError:
            return 0

    def print_info(self):
        print('Code: ', self.code)
        print('Name: ', self.name)
        print('Category: ', self.category)
        print('Price: ', self.price_sell)
        print('Application: ', self.application)
        print('Manufacture: ', self.manufacturer)

    def __str__(self):
        return self.name


class Orders:

    def __init__(self, date, order_by, total_price, product_list, profit):
        self.date = date
        self.order_by = order_by
        self.total_price = total_price
        self.product_list = product_list
        self.profit = profit

    def __str__(self):
        return self.date
