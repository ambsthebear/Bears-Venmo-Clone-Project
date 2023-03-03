user_one = {
    'full_name': 'Puppycat',
    'username': 'ActuallyAPrince247',
    'password': '2cute2POOT',
    'account_balance': 50.00,
    'connected_banks': [
        ('Thieves Bank', 1500.00),
        ('First Bank of the Multiverse', 355.00)
    ]
}

user_two = {
    'full_name': 'Catbug',
    'username': 'SugarPeasOK',
    'password': 'Throwablanketoverit!',
    'account_balance': 1.00,
    'connected_banks': [
        ('Warriors Credit Union', 15.00),
        ('First Bank of the Multiverse', 32.00)
    ]
}

import venmo_clone_functions

# venmo_clone_functions.authenticate_login(user_one)
venmo_clone_functions.show_banks(user_one)