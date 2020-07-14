def zero_right(list_):
    list_1 = []
    list_2 = []
    for el in list_:
        if el:
            list_1.append(el)
        else:
            list_2.append(el)
    list_1.extend(list_2)
    return list_1

if __name__ == '__main__':
    list_ = [0, 5, 2, 0, 0, 5, 23, 6, 0, 67]
    print(zero_right(list_))
