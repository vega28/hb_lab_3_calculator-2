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

def get_user_input():
    user_input = input('> ')
    tokens = user_input.split(' ')
    return tokens

tokens = ['']
while tokens[0] != 'q':

    tokens = get_user_input()

    if tokens[0] == '+':
        pass
    elif tokens[0] == '-':
        pass
    elif tokens[0] == '*':
        pass
    elif tokens[0] == '/':
        pass
    elif tokens[0] == 'square':
        pass
    elif tokens[0] == 'cube':
        pass
    elif tokens[0] == 'pow' or tokens[0] == 'power':
        pass
    elif tokens[0] == 'mod' or tokens[0] == '%':
        pass
    else:
        print('that is not valid input - please try again.')

print('okay, goodbye!') 


