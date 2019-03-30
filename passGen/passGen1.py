import random

characters = 'abcdefghijklmnopqrstuvwxyz1234567890!"£$%^&*()_+-=~{}.<>/?'

password = ''

for i in range(32):
    password += random.choice(characters)

print(password)
