def country(str_):
    list_ = str_.split('\n')
    dict_ = {}
    num = int(list_[0])
    for i in range(1, num+1):
        list_1 = list_[i].split()
        dict_[list_1[0]]= ' '.join(list_1[1:])

    for el in list_[num+2:]:
        if el == '':
            continue
        for key, val in dict_.items():
            if el in val:
                print(key)
                break

if __name__ == '__main__':
    str_ = '''2
    Russia Moscow Petersburg Novgorod Kaluga
    Ukraine Kiev Donetsk Odessa


    3
    Odessa
    Moscow
    Novgorod
    '''
    country(str_)
