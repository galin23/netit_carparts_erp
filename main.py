from helpers import login_menu, register

def sign_up_menu():
    while True:
        action = input('Please enter action:\n1 - for login\n2 for register')
        if action == '1':
            login_menu()
            break
        elif action == '2':
            register()
            break
        else:
            print('Please enter valid action!')
sign_up_menu()


