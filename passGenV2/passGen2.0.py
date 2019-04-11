import random


def passgen():
    char = 'abcdefghijklmnopqrstuvwxyz'
    numb = '1234567890'
    symb = '!"£$%^&*()_+-=~{}.<>/?'
    capital_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    characters = char + numb + symb + capital_char

    password = '\n'

    for i in range(32):
        password += random.choice(characters)

passgen()

