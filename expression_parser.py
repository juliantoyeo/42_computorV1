import re
from exit_handler import *
from utils import *
from classes.Terms import Terms
from classes.Expression import Expression


def getTerms(termsStr, showError):
    formattedStr = termsStr.replace('*', '')
    variable = "".join(re.findall("[a-zA-Z]+", formattedStr))
    if (len(variable) > 1):
        ft_exit_program_error(
            error_case['MULTIPLE_VARIABLES'], showError, termsStr)
    elif (len(variable) == 0):
        coefficient = formattedStr
        variable = ''
        degree = '0'
    else:
        coefficient_degree = formattedStr.split(variable)
        coefficient = (coefficient_degree[0], '1')[coefficient_degree[0] == '']
        degreeNumber = coefficient_degree[1].replace('^', '')
        havePowerSign = re.search('[\^]', coefficient_degree[1])
        if (havePowerSign == None and degreeNumber != ''):
            ft_exit_program_error(
                error_case['NO_POWER_SIGN'], showError, termsStr)
        elif (havePowerSign and degreeNumber == ''):
            ft_exit_program_error(
                error_case['NO_FOLLOW_UP_DEGREE'], showError, termsStr)
        degree = (degreeNumber, '1')[degreeNumber == '']
    try:
        float(coefficient)
    except ValueError:
        ft_exit_program_error(
            error_case['INVALID_COEFFICIENT'], showError, termsStr)
    try:
        int(degree)
    except ValueError:
        ft_exit_program_error(
            error_case['INVALID_DEGREE'], showError, termsStr)
    return {
        'coefficient': float(coefficient),
        'variable': variable,
        'degree': int(degree)
    }


def getTermsList(str, options):
    termsList = []
    termsStr = ''
    sign = '+'
    position = 'left'
    showError = (False, True)['e' in options]

    for char in str:
        if (char == '+' or char == '-' or char == '='):
            if (termsStr != ''):
                terms = getTerms(termsStr, showError)
                newTerms = Terms(sign, position, terms)
                termsList.append(newTerms)
                termsStr = ''
            if (char == '+'):
                sign = '+'
            elif (char == '-'):
                sign = '-'
            elif (char == '='):
                if (position == 'left'):
                    sign = '+'
                    position = 'right'
                else:
                    ft_exit_program_error(error_case['MORE_THEN_ONE_EQUAL'])
        else:
            termsStr += char
    terms = getTerms(termsStr, showError)
    newTerms = Terms(sign, position, terms)
    termsList.append(newTerms)
    return termsList


def checkUnsupportedSign(str, options):
    showError = (False, True)['e' in options]
    nonAlphaNumeric = re.findall("[^a-zA-Z\d+\-=\^*\.]", str)
    if (len(nonAlphaNumeric) != 0):
        ft_exit_program_error(
            error_case['UNSUPPORTED_CHARACTER'], showError, nonAlphaNumeric)


def getOptions(options):
    options = options.replace('-', '')
    return [char for char in options]


def parseArgv(argv):
    argc = len(argv)
    if (argc == 2 or (argc == 3 and argv[1].startswith('-'))):
        exp = ''
        options = []
        if (argc == 2):
            exp = argv[1]
        else:
            exp = argv[2]
            options = getOptions(argv[1])
        input = exp
        formattedInput = input.replace(' ', '')
        if (formattedInput == ''):
            return
        checkUnsupportedSign(formattedInput, options)

        termsList = getTermsList(formattedInput, options)
        expression = Expression(termsList, options)
        return expression
    else:
        ft_exit_program_error(error_case['WRONG_USAGE'])
