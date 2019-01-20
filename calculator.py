'''A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
'''

from arithmetic import *


# Your code goes here

run_calculator = True
while run_calculator:
    try:
        input_string = input('>').strip()
        tokens = input_string.split(' ')
        tokens = [item for item in tokens if len(item) != 0]
        if tokens[0] in ['+', '-', '*', '/', 'mod', 'pow'] and len(tokens) < 3:
            raise IndexError
        elif tokens[0] in ['square', 'cube'] and len(tokens) < 2:
            raise IndexError
        for i in range(1, len(tokens)):
            tokens[i] = float(tokens[i])
    except ValueError:
        print('You just entered some stuff that couldn\'t be calculated, re-enter')
        continue
    except IndexError:
        print('You didn\'t add enough arguments')
        continue
    if (tokens[0] == '+'):
        print(add(tokens[1], tokens[2]))
    elif tokens[0] == '-':
        print(subtract(tokens[1], tokens[2]))
    elif tokens[0] == '*':
        print(multiply(tokens[1], tokens[2]))
    elif tokens[0] == '/':
        try:
            print(divide(tokens[1], tokens[2]))
        except ZeroDivisionError:
            print('Can\'t divide by zero')
    elif tokens[0] == 'square':
        print(square(tokens[1]))
    elif tokens[0] == 'cube':
        print(cube(tokens[1]))
    elif tokens[0] == 'pow':
        print(power(tokens[1], tokens[2]))
    elif tokens[0] == 'mod':
        print(mod(tokens[1], tokens[2]))
    elif tokens[0] == 'q':
        run_calculator = False
    else: 
        print('Invalid arithmetic function. Try again')



