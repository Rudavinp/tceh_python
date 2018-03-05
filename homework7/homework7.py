import time
from functools import reduce

"""
Задание №1 (простое)
"""

"""
1.1 На map, filter, reduce написать программу, которая проверяет,
является ли строка палиндромом
"""


def is_palindrom_map(word):
    new_word = ''.join(map(lambda x: '' + x,  word[::-1]))
    return new_word == word


def is_palindrom_filter(word):
    new_word = ''.join(filter(lambda x: word.index(x) == word[::-1].index(x), word))
    return new_word == word


def is_palindrom_reduce(word):
    new_word = reduce(lambda a, b: a + b, word[::-1])
    return word == new_word


print(is_palindrom_map('rotar'))
print(is_palindrom_filter('rator'))
print(is_palindrom_reduce('rator'))
print('_____________')


"""
1.2 Написать декоратор, который замеряет время работы функции и вывод его
1.3 Переписать декоратор так, чтобы его можно было включать и выключать
"""


def switch(flag=True):
    def meter_speed_decor(func):
        def inner(*args):
            a = time.time()
            func(*args)
            b = time.time()
            if flag:
                print('time work:', round(((b - a)*1000), 3), 'sek')
        return inner
    return meter_speed_decor


@switch(True)
def some_fun(param):
    print('print', param)

some_fun('lol')


"""
1.4 Написать три декоратора, каждый декоратор выводит свое имя, так,
чтобы можно было написать их один над другим:
"""


def first_decorator(func):
    def iner(*args):
        print(first_decorator.__name__)
        return func(*args)
    return iner


def second_decorator(func):
    def iner(*args):
        print(second_decorator.__name__)
        return func(*args)
    return iner


def third_decorator(func):
    def iner(*args):
        print(third_decorator.__name__)
        return func(*args)
    return iner


@first_decorator
@second_decorator
@third_decorator
def foo(arg):
    print(arg)


"""
Задание №2 (посложнее)
Написать декоратор, который кеширует результат исполнения функции.
При повторном вызове с теми же аргументами функция не вызывается,
а результат выдается из кэша.
"""


def cash_func(func):
    cash = {}

    def iner(*args):
        if args in cash.keys():
            return cash[args]
        result = func(*args)
        cash[args] = result
        print(cash)
        print('Function called, result ', result)
        return result
    return iner


@cash_func
def lol_func(a, b, c):
    e = a + b + c
    return e

print(lol_func(1, 2, 3))
print(lol_func(3, 4, 5))
print(lol_func(1, 2, 3))


"""
Задание №3 (посложное)
Написать декоратор check, который проверяет типы входных аргументов
декорируемой функции и тип результата
"""


def check(func):
    def iner(*args):
        print(list(map(type, args)))
        result = func(*args)
        print(type(result))
        return result
    return iner


@check
def lol(a, b):
    return a + b


"""
Задание №4 (посложное)
Написать декоратор, который “пропускает” из функциии только один типа исключения
(RightError), все остальные превращая в исключения другого типа(WrongError)
"""


def catch_exception(func):
    def iner(*args):
        try:
            func(*args)
        except Exception as ex:
            if ex.__class__.__name__ == 'RightError':
                return ex.__class__.__name__
            else:
                return 'WrongError'
    return iner


@catch_exception
def some_func():
    return [5,1][5]

print(some_func())
