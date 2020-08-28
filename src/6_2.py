'''Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений (но не более n раз -
параметр декоратора). Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors
'''

class TooManyErrors(Exception):
    pass

def r(n):
    def dec(fun):
        def wrapper(args):
            nonlocal n
            try:
                if not n:
                    raise TooManyErrors
                f = fun(args)
                n -= 1
                return f
            except TooManyErrors:
                return

        return wrapper

    return dec



@r(4)
def f1(n):
    return n+1

print(f1(1))
print(f1(2))
print(f1(3))
print(f1(4))
print(f1(5))
print(f1(6))
