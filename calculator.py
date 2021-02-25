"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# loop through the following:
#   get user input as string
#   tokenize the string on spaces
#   identify the correct function using the first token
#       if the token is 'q', then quit
#       if the token is otherwise valid, then do the thing
#       if the token is broken, throw an error
#   evaluate the correct expression using the rest of the tokens
#   make sure end result is float (except for mod)

def get_user_input():
    user_input = input('> ')
    tokens = user_input.split(' ')
    return tokens

tokens = ['']
while tokens[0] != 'q':

    tokens = get_user_input()

    if tokens[0] == '+':
        result = add(float(tokens[1]),float(tokens[2]))
    elif tokens[0] == '-':
         result = subtract(float(tokens[1]),float(tokens[2]))
    elif tokens[0] == '*':
        result = multiply(float(tokens[1]),float(tokens[2]))
    elif tokens[0] == '/':
        result = divide(float(tokens[1]),float(tokens[2]))
    elif tokens[0] == 'square':
        result = square(float(tokens[1]))
    elif tokens[0] == 'cube':
        result = cube(float(tokens[1]))
    elif tokens[0] == 'pow' or tokens[0] == 'power':
        result = power(float(tokens[1]),float(tokens[2]))
    elif tokens[0] == 'mod' or tokens[0] == '%':
        result = int(mod(float(tokens[1]),float(tokens[2]))) # result should be int!
    else:
        result = 'that is not valid input - please try again.'
    print(result)

print('okay, goodbye!') 


