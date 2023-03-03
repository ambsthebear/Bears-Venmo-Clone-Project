def authenticate_login(user):
    valid_login = False

    while valid_login == False:
        username = input("Type your username: ")
        password = input("Type your password: ")

        if password == ((user)['password']) and username == ((user)['username']):
            print(f"Login Successful! Welcome, " + f"{user}!" )
            valid_login = True
        else:
            print("Login failed. Try again.")
            valid_login = False
    
    print(f"Your account balance is: " + f"{(user)['account_balance']}")

def show_banks(user):
    for bank_tuple in user ['connected_banks']:
        print(f"Your connected bank, " + f'{bank_tuple[0]}' + f", has a balance of " + f'{bank_tuple[1]}')

def select_bank():
    pass

def check_account_bal(user):
    xfer_amount = int[input("How much would you like to transfer? Please enter a whole dollar amount. ")]
    while xfer_amount > ((user)['account_balance']):
        print(f"You don't have enough in your account. Your account balance is " + f'{(user)['account_balance']}.') # Bonus code: + f"Please choose a connected bank to fund your account first.")
        # Bonus code: select_bank(user)

###
# Ask user_one if they would like to transfer money to user_two.
# If not, end the program.
# Ask user_one how much money they would like to transfer.
# If insufficient balance, re-prompt and print balance of account
# Add the transferred amount to user_two balance.
# Display the new balance of user_one’s account.
# Ask if the user would like to make another transfer.
# If yes, repeat the entire sequence.
# If not, print the final account balance of user_one and exit.

def confirm_xfer(user1, user2):
    start_xfer = input(f"Would you like to make a transfer to " + f'{user2}' + f"? (Y/N)")
    if start_xfer == 'Y':
        check_account_bal(user1)
    else:
        print("Goodbye!")


def update_account_balances():
    pass


