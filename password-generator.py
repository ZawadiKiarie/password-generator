import random

print('Welcome to your Password generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789'
number = int(input('Amount of passwords to generate: '))
pwd_length = int(input('Password length: '))
print('\nhere are your passwords: ')

for pwd in  range(number):
  password = ''
  for c in range(pwd_length):
    password += random.choice(chars)#gets a random character when provided a list of items in this case its a list of characters in a string
  print(password)
