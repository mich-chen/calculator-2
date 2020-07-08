"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# split user's input string into (prefix_opperand, num1, num2)
# example: 
# if the first token is 'pow':
    # call power function with the other two tokens (num1, num2)

"""repeat forever:
    read input
    tokenize input
        if the first token is "q":
            quit
        else:
            (decide which math function to call based on first token)
            if the first token is 'pow':
                  call the power function with the other two tokens

            (...etc.)"""

def tokenize(string):
    """ Tokenizes a string into a list """

    tokens = string.split(' ')
    # split string at spaces and store the list into token_string

    return tokens


while True: