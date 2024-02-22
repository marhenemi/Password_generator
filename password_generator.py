import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789#£%&?+_-'
password = ''
for x in range(16):
    password += random.choice(chars)

print(f"Your generated password is: \n{password}")