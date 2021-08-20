from re import X
import sys
from expression_parser import *

#able to accept any character for variable but the variable must be the samme accros all terms
#x is the same as X

# acceptable  form
"X"
"x"
"0 * x" or "x"
"0 * x^0"
"1 * x^0" or "x^0"
"1 * x^1" or "x^1" or "1x"
"2 * x^1" or "2x^1" or "2x"



if __name__ == '__main__':
    expList = [
        "",
        "x",
        "xy",
        "x^1",
        "x1",
        "x^",
        "x^1.2",
        "!",
        "-",
        "+",
        "=",
        "^",
        "*",
        "x^1 = x^1 = 0",
        "2x + 2y",
        "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
        "42 * X^0 = 42 * X^0",
        "4 * X ^ 0 = 8 * X ^ 0",
        "5 * X ^ 0 = 5 * X ^ 0",
        "5 * X^0 + 4 * X^1 = 4 * X^0",
        "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
        "5 + 4 * X + X^2= X^2",
        "5 * X ^ 0 = 4 * X ^ 0 + 7 * X ^ 1",
        "5 * X ^ 0 + 13 * X ^ 1 + 3 * X ^ 2 = 1 * X^0 + 1 * X^1",
        "6 * X ^ 0 + 11 * X ^ 1 + 5 * X ^ 2 = 1 * X ^ 0 + 1 * X ^ 1",
        "5 * X ^ 0 + 3 * X ^ 1 + 3 * X ^ 2 = 1 * X ^ 0 + 0 * X^1",
    ]

    argc = len(sys.argv)
    options = '-x'
    if (argc == 2):
        index = int(sys.argv[1])
    else:
        options = sys.argv[1]
        index = int(sys.argv[2])

    exp = expList[index]
    print(f'Test number "{index}" \n======================')
    print(f'testing "{exp}"')
    expression = parseArgv(["", options, exp])
    if (expression):
        expression.solver()
