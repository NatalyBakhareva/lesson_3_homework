import re


class Calculator:
    def __init__(self):
        self.base_numeral_system = 10

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    operation = {
        '*': lambda self, x, y: Calculator.multiply(self, x, y),
        '/': lambda self, x, y: Calculator.divide(self, x, y),
        '+': lambda self, x, y: Calculator.add(self, x, y),
        '-': lambda self, x, y: Calculator.subtract(self, x, y)
    }
    operations = ['/', '*', '-', '+']

    def evaluate(self, expression):  # вычисление простых выражений без скобок
        expr = re.split('([\d\.]+)', expression)
        for op in Calculator.operations:
            i = 1
            while i < (len(expr) - 1):
                if expr[i] == op:
                    expr[i - 1] = str(Calculator.operation[op](self, float(expr[i - 1]), float(expr[i + 1])))
                    del expr[i]
                    del expr[i]
                    i -= 1
                i += 1
        return expr[1]

    def evaluatepar(self, expressions):  # поиск и вычисление выражений в скобках
        reg = re.compile('\([\d\.\*/\+-]*\)')
        if len(re.findall('\(', expressions)) != len(re.findall('\)', expressions)):
            raise SyntaxError('Незакрытые скобки')
        while reg.search(expressions) != None:
            ex = reg.search(expressions).group()
            new_ex = Calculator.evaluate(self, ex)
            expressions = reg.sub(new_ex, expressions, count=1)
        return expressions

