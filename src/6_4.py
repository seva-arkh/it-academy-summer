'''Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для
определения количества чисел, меньших n, которые взаимно просты с n. К примеру,
т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и взаимно просты с девятью, φ(9) = 6.
Число 1 считается взаимно простым для любого положительного числа,
так что φ(1) = 1.

Интересно, что φ(87109) = 79180, и, как можно заметить, 87109 является
перестановкой 79180.

Найдите такое значение n, 1 < n < 10**6, при котором φ(n) является
перестановкой n, а отношение n/φ(n) является минимальным.
'''

import sympy

def phi(n):
    result = n
    i = 2

    while i*i<=n:
        if not n%i:
            while not n%i:
                n /= i
            result -= result/i
        i += 1

    if n>1:
        result -= result/n

    return result

def task_70():
    min = [21,21/12]
    k = 2
    lis=[]
    max_i = 10**6
    l_pr = list(sympy.primerange(0, max_i))

    for i in range(max_i+2):
        lis.append(0)


    for i in l_pr[1:]:
        lis[i] = i-1
        p = i*i
        f = i
        while p<max_i:
            lis[p] = p - f
            f = p
            if p/lis[p] < min[1] and sorted(str(p)) == sorted(str(lis[p])):
                min = [p,p/lis[p]]
            p *= i


    len_ = len(lis)
    for i in range(2, len_):
        if not lis[i]:
            lis[i] = int(phi(i))
            if i/lis[i] < min[1] and sorted(str(i)) == sorted(str(lis[i])):
                min = [i,i/lis[i]]

    return min[0]

print(task_70())
