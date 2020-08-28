'''Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. 
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
'''

import functions

def runner(*args):
    f = [el for el in dir(functions) if callable(getattr(functions,el))]

    if args:
        for el in args:
            try:
                print(getattr(functions,el)())
            except:
                print('There is no such function: '+el)

    else:
        for el in f:
            print(getattr(functions,el)())
    return

runner()
runner('b_5')
runner('b_5','b_7')
