from time import time, sleep

def measure_time(func):
    """ Декоратор вычисления времени работы функции """

    def decorator(*args, **kwargs):
        t1 = time()
        func()
        t2 = time()
        delta = t2 - t1
        return delta # возвращаем время работы функции
    return decorator


def f1():
    """ Функция 1 """
    sleep(.5)
    return 'f1 result'


def f2():
    """ Функция 2 """
    sleep(.5)
    return 'f2 result'

def f3():
    """ Функция 3 """
    sleep(1)
    return 'f3 result'

# декорируем функции, чтобы в результате они вычисляли время работы функции
f1_decorated = measure_time(f1)
f2_decorated = measure_time(f2)
f3_decorated = measure_time(f3)

# узнаём время работы функции
time_of_f1 = f1_decorated()
time_of_f2 = f2_decorated()
time_of_f3 = f3_decorated()

# выводим полученные данные
print('Время работы f1:', round(time_of_f1, 2))
print('Время работы f2:', round(time_of_f2, 2))
print('Время работы f3:', round(time_of_f3, 2))