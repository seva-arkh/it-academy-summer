def num_diff_words (str_):
    list_ = str_.split()
    set_ = set()
    for el in list_:
        set_.add(el)
    return len(set_)

if __name == '__main__':
    str_ = '12 24 4$ 32   5 6'
    print(num_diff_words(str_))
