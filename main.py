import re
from calculator import Calculator

print('Калькулятор 1.0\nВвведите математическое выражение (например, 2*(3+2)) и нажмите Enter.\n'
      'Поддерживаемые операции: сложение, вычитание, умножение и деление.\n'
      'Если хотите закончить вычисления введите - exit.')
while True:
    str_input = input()
    str_input = str_input.replace(' ', '')
    if str_input == 'exit':
        exit()
    else:
        reg = re.compile('[^\(\)\d\*\+/-]+')
        if reg.search(str_input) == None:
            exp = Calculator()
            try:
                print('Ответ:', exp.evaluate(exp.evaluatepar(str_input)))
            except ZeroDivisionError:
                print('Ошибка: деление на ноль!')
            except IndexError:
                print('Ошибка: Вы не ввели математическое выражение или одна из скобок пустая!')
            except SyntaxError:
                print('Ошибка: незакрытые скобки!')
        else:
            print('Математическое выражение введено с недопустимыми символами:', end=' ')
            incorr_chars = reg.finditer(str_input)
            for match in incorr_chars:
                print(match.group(), end="")
            print()
