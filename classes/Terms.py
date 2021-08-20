from utils import *


class Terms:
    def __init__(self, sign, position, terms):
        # If the terms original position is on the right side, convert the sign
        sign = (sign, ft_convert_sign(sign))[position == 'right']
        self.coefficient = (terms['coefficient'],
                            terms['coefficient'] * -1)[sign == '-']
        self.variable = terms['variable']
        self.degree = terms['degree']
