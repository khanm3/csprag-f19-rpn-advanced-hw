#!/usr/bin/env python3

import operator
import readline
from colorama import Fore, Style

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '^': operator.pow,
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)

        #print(stack)
    if len(stack) != 1:
        raise TypeError('malformed input')
    return stack.pop()

def colored_output(expression, result):
    tokens = expression.split()
    arg1 = int(tokens[0])
    arg2 = int(tokens[1])
    operator = tokens[2]
    s = ''

    def bright_red(arg):
        return Style.BRIGHT + Fore.RED + str(arg) + Style.RESET_ALL

    if (arg1 < 0):
        s += bright_red(arg1)
    else:
        s += str(arg1)

    s += Fore.GREEN + ' ' +  operator + ' ' + Fore.RESET

    if (arg2 < 0):
        s += bright_red(arg2)
    else:
        s += str(arg2)

    s += ' = ' + str(result)

    return s

def main():
    while True:
        expression = input('rpn calc> ')
        result = calculate(expression)
        print(colored_output(expression, result))

if __name__ == '__main__':
    main()
