import copy
from exit_handler import *
from utils import *


class Expression:
    def __init__(self, termsList, options):
        self.originalExp = termsList
        reducedForm, a, b, c = self.getReducedForm()
        self.reducedForm = reducedForm
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = self.getDiscriminant()
        self.highestDegree = self.getHighestDegree()
        self.options = options

    def getHighestDegree(self):
        highestDegree = 0
        for terms in self.reducedForm:
            if (terms.degree > highestDegree and terms.coefficient != 0):
                highestDegree = terms.degree
        return highestDegree

    def getReducedForm(self):
        newExp = copy.deepcopy(self.originalExp)
        a = 0
        b = 0
        c = 0
        i = 0
        for terms in newExp:
            currentTerms = terms
            i += 1
            j = i
            # to iterate through the rest if the list to get the terms with the same degree, add it ups and remove that terms from the list
            # also to check if the original expression contains different variable
            while j < len(newExp):
                if (currentTerms.variable != '' and newExp[j].variable != '' and currentTerms.variable.lower() != newExp[j].variable.lower()):
                    ft_exit_program_error(error_case['DIFFERENT_VARIABLES'])
                if (newExp[j].degree == currentTerms.degree):
                    matchedTerms = newExp[j]
                    currentTerms.coefficient = matchedTerms.coefficient + currentTerms.coefficient
                    del newExp[j]
                else:
                    j += 1
            if (currentTerms.degree == 0):
                c = currentTerms.coefficient
            elif (currentTerms.degree == 1):
                b = currentTerms.coefficient
            elif (currentTerms.degree == 2):
                a = currentTerms.coefficient
        return newExp, a, b, c

    def getDiscriminant(self):
        discriminant = ft_power(self.b, 2) - 4 * self.a * self.c
        return discriminant

    def printReduceForm(self):
        highestCoefficient = self.reducedForm[0].coefficient
        message = 'Reduced form:'
        for index, terms in enumerate(self.reducedForm):
            if (terms.coefficient > highestCoefficient):
                highestCoefficient = terms.coefficient
            if (terms.coefficient < 0):
                message += ' -'
            elif (index != 0):
                message += ' +'
            message += f' {str(ft_convert_if_integer(terms.coefficient)).replace("-", "")}'
            if (terms.variable != ''):
                message += f' * {terms.variable}^{terms.degree}'
        message += f' = 0'
        print(message)
        print(f'Polynomial degree: {self.highestDegree}')
        if (highestCoefficient == 0):
            ft_exit_program_error(error_case['ALL_REAL_NUMBERS_ARE_SOLUTIONS'])

    def printDiscrimant(self):
        if (self.discriminant > 0):
            print('Discriminant is strictly positive, the two solutions are:')
        elif (self.discriminant < 0):
            print('Discriminant is strictly negative, the two complex solutions are:')
        else:
            print('Discriminant is equal to 0, the solution is:')

    def solver_two_degree(self):
        denominator = 2 * self.a
        discriminantSqrt = ft_sqrt(self.discriminant)
        solution1 = (-1 * self.b) - discriminantSqrt
        solution2 = (-1 * self.b) + discriminantSqrt

        if ('s' in self.options):
            print(f'\nSolution steps:')
            print(f'Step 1:')
            print(f'- find discriminant (b^2 - 4ac)')
            print(f'- a = {self.a} b = {self.b} c = {self.c}')
            print(f'- {self.b}^2 - 4 * {self.a} * {self.c}')
            print(f'- discriminant = {self.discriminant}')
            print(f'\n')
            print(f'Step 2:')
            print(f'- apply quadratic equation formula (-b ± sqrt(b^2 - 4ac) / 2a)')
            print(f'- or (-b ± sqrt(discriminant) / 2a)')
            print(
                f'- a = {self.a} b = {self.b} c = {self.c} discriminant = {self.discriminant}')
            print(f'- -({self.b}) ± sqrt({self.discriminant}) / 2 * {self.a})')
            print(f'\n')
        if (self.discriminant > 0):
            print('Discriminant is strictly positive, the two solutions are:')
            print('%.6f' % (solution1 / denominator))
            print('%.6f' % (solution2 / denominator))
        elif (self.discriminant < 0):
            print('Discriminant is strictly negative, the two complex solutions are:')
            print('%.6f' % (-self.b / (2 * self.a))+' + i * %.6f' %
                  (ft_sqrt(-self.discriminant) / (2 * self.a)))
            print('%.6f' % (-self.b / (2 * self.a))+' - i * %.6f' %
                  (ft_sqrt(-self.discriminant) / (2 * self.a)))
        else:
            print('Discriminant is equal to 0, the solution is:')
            print('%.6f' % (solution1 / denominator))

    def solver_one_degree(self):
        solution = (-1 * self.c) / self.b
        print('The solution is:')
        print('%.6f' % solution)

    def solver_zero_degree(self):
        ft_exit_program_error(error_case['NO_SOLUTION'])

    def solver(self):
        self.printReduceForm()
        if (self.highestDegree > 2):
            ft_exit_program_error(error_case['MORE_THEN_DEGREE_TWO'])
        elif (self.highestDegree == 2):
            self.solver_two_degree()
        elif (self.highestDegree == 1):
            self.solver_one_degree()
        elif (self.highestDegree == 0):
            self.solver_zero_degree()
