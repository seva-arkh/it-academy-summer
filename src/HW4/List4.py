def diff_el_in_one (list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    num_1 = 0
    num_2 = 0
    for el in set_1:
        if el not in set_2:
            num_1 += 1
    for el in set_2:
        if el not in set_1:
            num_2 += 1
    return num_1, num_2

if __name == '__main__':
    list_1 = [3,6,4,1,0,2,1,6,7]
    list_2 = [3,5,11,34,6,2,7]
    print(diff_el_in_one(list_1, list_2))
