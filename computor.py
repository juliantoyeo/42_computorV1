import sys
if (sys.version_info.major != 3):
    sys.exit('Sorry, requires Python 3')
from expression_parser import *


if __name__ == '__main__':
    expression = parseArgv(sys.argv)
    expression.solver()
