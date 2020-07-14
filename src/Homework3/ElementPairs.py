import math

def cout_pairs(str_):
    list_ = str_.split()
    set_ = set()
    num_of_pairs = 0
    for el in list_:
        if el not in set_:
            num = list_.count(el)
            num_of_pairs += int(math.factorial(num)/(math.factorial(num-2)*2))
            set_.add(el)
    return num_of_pairs

if __name__ == '__main__':
    str_ = '1 1 1 1'
    print(cout_pairs(str_))
