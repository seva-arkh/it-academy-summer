import copy

el_1 = ['a', 'b']
el_2 = ['b', 'c', 'd']
list_ = [ x  +y for x in el_1 for y in el_2]
list_ = list_[::2]
list_1 = [str(num) + 'a' for num in range(1,5)]
print(list_1.pop(1))
list_12 = copy.copy(list_1)
list_12.append('2a')
print(list_12)
