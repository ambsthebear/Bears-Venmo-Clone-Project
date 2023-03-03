def authenticate_login(user):
    valid_login = False

    while valid_login == False:
        username = input("Type your username: ")
        password = input("Type your password: ")

        if password == ((user)['password']) and username == ((user)['username']):
            print("Login Successful!")
            valid_login = True
        else:
            print("Login failed. Try again.")
            valid_login = False

def select_bank():
    pass

def confirm_xfer():
    pass

def update_account_balances():
    pass


