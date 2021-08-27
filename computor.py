import sys
if (sys.version_info.major != 3):
    sys.exit('Sorry, requires Python 3')
from expression_parser import *
from exit_handler import *


if __name__ == '__main__':
    expression = parseArgv(sys.argv)
    if (expression):
        expression.solver()

