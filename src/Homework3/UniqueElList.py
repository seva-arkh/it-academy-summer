def one_time(list_):
    set_ = set()
    new_list = []
    for el in list_:
        if el not in set_:
            if list_.count(el) == 1:
                new_list.append(el)
            else:
                set_.add(el)
    return new_list

if __name__ == '__main__':
    list_ = [5, 2, 1, 10, 3, 2, 4, 5]
    print(one_time(list_))
