import sys

error_case = {
    'WRONG_USAGE': 'WRONG_USAGE',
    'UNSUPPORTED_CHARACTER': 'UNSUPPORTED_CHARACTER',
    'MULTIPLE_VARIABLES': 'MULTIPLE_VARIABLES',
    'DIFFERENT_VARIABLES': 'DIFFERENT_VARIABLES',
    'NO_POWER_SIGN': 'NO_POWER_SIGN',
    'NO_FOLLOW_UP_DEGREE': 'NO_FOLLOW_UP_DEGREE',
    'INVALID_COEFFICIENT': 'INVALID_COEFFICIENT',
    'INVALID_DEGREE': 'INVALID_DEGREE',
    'MORE_THEN_DEGREE_TWO': 'MORE_THEN_DEGREE_TWO',
    'MORE_THEN_ONE_EQUAL': 'MORE_THEN_ONE_EQUAL',
    'ALL_REAL_NUMBERS_ARE_SOLUTIONS': 'ALL_REAL_NUMBERS_ARE_SOLUTIONS',
    'NO_SOLUTION': 'NO_SOLUTION'
}


def ft_exit_program_error(case, showError = False, errorCause=''):
    if (showError and errorCause != ''):
        print(f'Error on "{errorCause}"')
    if (case == error_case['WRONG_USAGE']):
        print(f'usage : python3 computor.py [options] [equation string]')
        print(f'options :')
        print(f'\t-s, to display solution steps')
        print(f'\t-e, to display error')
        sys.exit(1)
    if (case == error_case['UNSUPPORTED_CHARACTER']):
        sys.exit(f'The expression contained unsupported character(s)')
    if (case == error_case['MULTIPLE_VARIABLES']):
        sys.exit(f'Sorry, only 1 variable per terms is allowed')
    if (case == error_case['DIFFERENT_VARIABLES']):
        sys.exit(f'Sorry, only support 1 kind of variable')
    if (case == error_case['NO_POWER_SIGN']):
        sys.exit(f'Sorry, please use "^" to represent power sign')
    if (case == error_case['NO_FOLLOW_UP_DEGREE']):
        sys.exit(
            f'Sorry, if a power sign "^" is used, please follow up by a number to represent the degree')
    if (case == error_case['INVALID_COEFFICIENT']):
        sys.exit(f'Sorry the coefficient must be valid number')
    if (case == error_case['INVALID_DEGREE']):
        sys.exit(f'Sorry the degree must be valid number')
    if (case == error_case['MORE_THEN_DEGREE_TWO']):
        sys.exit(f'The polynomial degree is strictly greater than 2, I can\'t solve.')
    if (case == error_case['MORE_THEN_ONE_EQUAL']):
        sys.exit('Sorry, the program only allowed 1 "=" sign')
    if (case == error_case['ALL_REAL_NUMBERS_ARE_SOLUTIONS']):
        sys.exit(
            'The reduced form comes down to 0 = 0, therefore all real numbers are solutions')
    if (case == error_case['NO_SOLUTION']):
        sys.exit(f'Both side is not equal, there is no solution')
