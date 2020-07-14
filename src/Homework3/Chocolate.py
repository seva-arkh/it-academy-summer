#1
def one_break(m, n, k):
    if not k%m or not k%n:
        return True
    return False

''' Делаю дерево допустим размеры шоколадки это 2*2
        [2,2]
    [1,2]   [2,1]
и так далее
В функции k_pieces мы перебираем проходим по дереву находя хотя бы
один вариант который пашет
и добавляем в x эти комбинации

далее проходим все варианты в x и если t == m-x[i][0]+n-x[i][1]
тогда можно за такое колличество разломов
'''
#2
class Tree(object):
    def __init__(self, a=0, b=0):
        self.left = None
        self.right = None
        self.data = [a,b]

def tree_(root, m, n):
    if m:
        root.left = Tree(m-1, n)
        tree_(root.left, m-1, n)
    if n:
        root.right = Tree(m, n-1)
        tree_(root.right, m, n-1)


def k_pieces(root, k, x, k1):
    if k1 == root.data[0]*root.data[1]:
        x.append(root.data)
    if k == 0:
        x.append(root.data)
        return True
    if k<root.data[0] and k<root.data[1]:
        return False
    return k_pieces(root.left, k-root.data[1], x, k1) or \
    k_pieces(root.right, k-root.data[0], x, k1)

#3
def k_for_t(t, m, n, x):
    for el in x:
        if t == m-el[0]+n-el[1]:
            return True
    return False



if __name__ == '__main__':
    m, n, k = 3, 2, 4
    print(one_break(m, n, k))
    root = Tree(m, n)
    tree_(root, m, n)
    x=[]
    if m*n>=k:
        k_pieces(root, k, x, k)
    if x:
        print(True)
        t = 2
        print(k_for_t(t, m, n, x))
    else:
        print(False)
