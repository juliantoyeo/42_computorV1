def ft_abs(n):
    if n < 0:
        return -n
    return n


def ft_power(n, p):
    return n**p


def ft_sqrt(n):
    return n**0.5


def ft_convert_sign(sign):
    if (sign == '+'):
        return '-'
    return '+'


def ft_convert_if_integer(number):
    if (number.is_integer()):
        return int(number)
    return number


def ft_print_list_of_class(text, list):
    for item in list:
        ft_print_class_atr(text, item)


def ft_print_class_atr(text, cls):
    attrs = vars(cls)
    print(f'{text}{attrs.items()}')
