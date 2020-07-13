"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """

    fib_2 = 1
    for el in range(n):
        if not el:
            fib_1=0
            continue
        fib_2, fib_1 = fib_2 + fib_1, fib_2
    return fib_2  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 5
    print(fibonacci(n))
