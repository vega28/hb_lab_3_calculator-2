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

    while True:
        tokens = get_user_input()
        if tokens[0] == 'q': break
        
        # check that user input is valid:
        try:
            if len(tokens) > 1:
                num1 = float(tokens[1])
            # check for correct number of tokens
            if len(tokens) == 3: 
                if tokens[0] != 'square' and tokens[0] != 'cube':
                    num2 = float(tokens[2])
                    break
                else:
                    print('You have too many inputs. Please try again.')
            elif len(tokens) > 3:
                print('You have too many inputs. Please try again.')
            elif (tokens[0] != 'square' and tokens[0] != 'cube' and len(tokens) < 3) or len(tokens) <= 1:
                print('You need more inputs. Please try again.')
            else: break # if first token is square or cube and num1 is valid
        except ValueError:
            print('That is not valid input. Please try again.')
            print('Your entry should be of the format "operator number_1 (number_2)"')

    # perform the appropriate task
    if tokens[0] == '+':
        result = add(num1, num2)
    elif tokens[0] == '-':
         result = subtract(num1, num2)
    elif tokens[0] == '*':
        result = multiply(num1, num2)
    elif tokens[0] == '/':
        result = divide(num1, num2)
    elif tokens[0] == 'square':
        result = square(num1)
    elif tokens[0] == 'cube':
        result = cube(num1)
    elif tokens[0] == 'pow' or tokens[0] == 'power':
        result = power(num1, num2)
    elif tokens[0] == 'mod' or tokens[0] == '%':
        result = int(mod(num1, num2)) # result should be int!
    elif tokens[0] == 'q':
        result = 'Okay, goodbye!'
    else:
        result = 'That is not valid operator. Please try again. \nYour options are +, -, *, /, square, cube, pow, mod'
    print(result)


