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

# prompt user input
print('''Write your equation in prefix notation and we\'ll solve it for you! 
Please use +, -, *, /, square, cube, pow, or mod for prefix notation.
Press q to exit.\n\n''')

while True:
    
    string = input('Enter equation your equation >> ')
    tokens = tokenize(string)
    # tokens is now a list of strings 
    if tokens[0] == 'q':
        exit()
    else:
        # determine which function to call based on 1st token
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        # changed the strings into integers and assigned to num1 and num2
        if tokens[0] == '+':
            print(add(num1, num2))









