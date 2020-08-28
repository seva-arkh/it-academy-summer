'''Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
'''

def get_ranges(list_):
    str_ = ''
    el_1 = list_[0]
    list_1 = []
    while len(list_)>1:
        for i in range(len(list_)-1):
            if list_[i]+1 == list_[i+1]:
                if i+2 == len(list_):
                    list_1.append(str(list_[0])+'-'+str(list_[i+1]))
                    list_ = []
                pass
            else:
                if list_[0]!=list_[i]:
                    list_1.append(str(list_[0])+'-'+str(list_[i]))
                else:
                    list_1.append(''+str(list_[i]))
                list_ = list_[i+1:]
                break
    if list_:
        list_1.append(''+str(list_[0]))
    return ','.join(list_1)

if __name__ == '__main__':
    list_ = [0, 1, 2, 3, 4, 7, 8, 10]
    print(get_ranges(list_))
