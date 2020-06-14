import string
"""Найти самое длинное слово в введенном предложении. В случае если их
    несколько, самое левое в строке Учтите что в предложении есть знаки
    препинания.
"""


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """

    punctuation = ',.;\|/?><()!@'
    new_string = ''
    for el in str_:
        if el not in string.punctuation:
            new_string += el

    list = new_string.split(" ")
    max_len = 0
    word = ''
    for el in list:
        if len(el)>max_len:
            word=el
            max_len=len(el)
    return word  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = '{} wordddd {} wordd  '
    print(longest_word(str_))
