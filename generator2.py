'''
Parameters for password:
Length
Amount of digits
Amount of upper case
Amount of lower case
Amount of special characters
'''

import random

DIGITS = '0123456789'
LETTERS = 'abcdefghijklmnpqrstuvwxyz'
SPECIAL_CHARS = ',.-!?+-*/#"¤%&)(][}{~^¨½§€$£@`<>|'

def user_input(message: str) -> int:
    while True:
        try:
            return int(input(message))

        except ValueError:
            print('Provided amount must be a whole number')

            continue

length = user_input('Provide the desired length for the password: ')
digits_amount = user_input('Provide the desired amount of digits for the password: ')
letters_upper_amount = user_input('Provide the desired amount of upper case letters for the password: ')
special_amount = user_input('Provide the desired amount of special characters for the password: ')

password = ''

letters = length - digits_amount - letters_upper_amount - special_amount

for _ in range(letters):
    password += random.choice(LETTERS)

for _ in range(letters_upper_amount):
    password += random.choice(LETTERS).upper()

for _ in range(digits_amount):
    password += random.choice(DIGITS)

for _ in range(special_amount):
    password += random.choice(SPECIAL_CHARS)

print(password)
