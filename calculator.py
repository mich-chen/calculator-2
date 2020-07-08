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

def tokenize(input_string):
    """ Tokenizes a string into a list """

    token_string = string.split(' ')
    # split string at spaces and store the list into token_string

    return token_string


while True:
    # prompt user input
    print('Write your equation in prefix notation and we\'ll solve it for you!')
    string = input('Enter equation your equation >> ')
    tokens = tokenize(string)
    print(tokens)
    break
    


