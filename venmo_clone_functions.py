def authenticate_login(user):
    valid_login = False

    while valid_login == False:
        username = input("Type your username: ")
        password = input("Type your password: ")

        if password == ((user)['password']) and username == ((user)['username']):
            print(f"Login Successful! Welcome, " + f"{(user)['full_name']}!" )
            valid_login = True
        else:
            print("Login failed. Try again.")
            valid_login = False
    
    print(f"Your account balance is: " + f"{(user)['account_balance']}")

def show_banks(user):
    for bank_tuple in user ['connected_banks']:
        print(f"Your connected bank, " + f'{bank_tuple[0]}' + f", has a balance of " + f'{bank_tuple[1]}')

def check_account_bal(user1,user2):
    xfer_amount = input("How much would you like to transfer? Please enter a whole dollar amount. ")
    amount_to_check = int(xfer_amount)
    if amount_to_check > ((user1)['account_balance']):
        print(f"You don't have enough in your account. Your account balance is " + f"{(user1)['account_balance']}.")
        fund_account(user1)
        
    else:
        user1['account_balance'] = (((user1)['account_balance']) - amount_to_check)
        user2['account_balance'] = (((user2)['account_balance']) + amount_to_check)
        print(f"Your transfer was successful! Your account balance is now " + f"{(user1)['account_balance']}.")
        complete_xfer(user1, user2)

def confirm_xfer(user1, user2):
    start_xfer = input(f"Would you like to make a transfer to " + f"{(user2)['full_name']}" + f"? (Y/N)")
    if start_xfer == 'Y':
        check_account_bal(user1, user2)
    else:
        print("Goodbye!")
    
def complete_xfer(user1, user2):
    end_xfer = input(f"Would you like to make another transfer to " + f"{(user2)['full_name']}" + f"? (Y/N)")
    if end_xfer == 'Y':
        check_account_bal(user1, user2)
    else:
        print("Your final balance is " + f"{(user1)['account_balance']}.")
        print("Goodbye!")


def fund_account(user):
    bank_xfer = input("Would you like to transfer funds from a connected bank? (Y/N) ")
    if bank_xfer == 'Y':
        xfer_funds(user)
    else:
        print('OK. Goodbye!')
            

def xfer_funds(user):
    xfer_from_account = input(f"Please select your connected bank, " + f"{(user)['connected_banks'][0][0]}" + f" or {(user)['connected_banks'][1][0]}. ")
    if xfer_from_account == (user['connected_banks'][0][0]):
        amount_to_xfer = input('How much would you like to transfer from the selected account? Please enter a full dollar amount. ')
        funds_from_bank = int(amount_to_xfer)
        user['account_balance'] = (((user)['account_balance']) + funds_from_bank)                
        temp_bank_and_balance = list((user)['connected_banks'][0])
        temp_bank_and_balance[1] = (temp_bank_and_balance[1]) - funds_from_bank
        user['connected_banks'][0] = tuple(temp_bank_and_balance)
        print (f"Your transfer was successful! Your account balance is now " + f"{user['account_balance']}. " + "Your connected bank, " + f"{(user)['connected_banks'][0][0]}" + f", has a balance of " + f"{(user)['connected_banks'][0][1]}")
    elif xfer_from_account == (user)['connected_banks'][1][0]:
        amount_to_xfer = input('How much would you like to transfer from the selected account? Please enter a full dollar amount. ')
        funds_from_bank = int(amount_to_xfer)
        user['account_balance'] = (((user)['account_balance']) + funds_from_bank)
        temp_bank_and_balance = list((user)['connected_banks'][1])
        temp_bank_and_balance[1] = (temp_bank_and_balance[1]) - funds_from_bank
        user['connected_banks'][1] = tuple(temp_bank_and_balance)
        print (f"Your transfer was successful! Your account balance is now " + f"{user['account_balance']}. " + "Your connected bank, " + f"{(user)['connected_banks'][1][0]}" + f", has a balance of " + f"{(user)['connected_banks'][1][1]}")
    else:
        print('Sorry, that is not one of your connected banks. Goodbye!')