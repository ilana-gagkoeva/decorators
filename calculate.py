def log_errors(func):
    """ Декоратор логирования ошибок """

    def decorator(a, b, oper):
        try:
            return func(a, b, oper)
        except:
            msg = 'Функция {} выдала ошибку с параметрами: a={}, b={}, oper={}'.format(func.__name__, a, b, oper)
            print(msg)

        return None

    return decorator

@log_errors
def calculate(a: int, b: int, oper: str):
    """ Функция выполнения арифметической операции между двумя числами """

    expression = '{} {} {}'.format(a, oper, b)
    res = eval(expression)
    return res

r = calculate(1, 2, '+')
print(r)

r = calculate(1, None, '+')
print(r)