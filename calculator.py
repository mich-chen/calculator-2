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



def integered_nums(str_lst):
    """ converts string elements in a list into integers and returns a list"""

    num_lst = [int(str_lst[i]) for i in range(1, len(str_lst))]
    return (num_lst)

# prompt user input
print('''Write your equation in prefix notation and we\'ll solve it for you! 
Please use +, -, *, /, square, cube, pow, or mod for prefix notation.
Press q to exit.\n\n''')

def calc():
    """ calculate using prefix notation """

    while True:
        
        string = (input('Enter equation your equation >> '))
        tokens = string.split(' ')
        number_lst = integered_nums(tokens)
        operand = tokens[0]

        if tokens[0] == 'q':
            exit()

        if len(number_lst) > 1:
            # determine which function to call if user input gave two numbers
            """num1 = int(tokens[1])
            num2 = int(tokens[2])"""

            # changed the strings into integers and assigned to num1 and num2
            if operand == '+':
                print(add(number_lst[0], number_lst[1]))
            if operand == '-':
                print(subtract(number_lst[0], number_lst[1]))
            if operand == '*':
                print(multiply(number_lst[0], number_lst[1]))
            if operand == '/':
                print(divide(number_lst[0], number_lst[1]))
            if operand == 'pow':
                print(power(number_lst[0], number_lst[1]))
            if tokens[0] == 'mod':
                print(mod(number_lst[0], number_lst[1]))

        else:

            if operand == 'square':
                print(square(number_lst[0]))
            if operand == 'cube':
                print(cube(number_lst[0]))
            

calc()


    











