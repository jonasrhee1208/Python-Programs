import time
import random
import math
import sys
import os
from random import randint
blimey = randint(3,9)
print("Starting up...")
time.sleep(blimey)
print("Start up complete.")
print("Welcome  to calculator ++.")
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
''')
    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    elif operation == '**':
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1 ** number_2)
    elif operation == '%':
        print('{} % {} = '.format(number_1, number_2))
        print(number_1 % number_2)
    else:
        print('You have not typed a valid operator.')
    again()
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
        time.sleep(3)
        os._exit(0)
    else:
        again()
calculate()
