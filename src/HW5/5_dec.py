'''Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
'''

def dec(fn):
    def wrapper(a):
        n = fn(a)
        fl = open("dec_results.txt", "a")
        fl.write(str(n) + ' ')
        return n
    return wrapper


@dec
def f1(n):
    return n+1

f1(1)
f1(2)
f1(3)
f1(4)
