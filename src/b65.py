def b_5(n):
    if n<1:
        return False
    i=0
    n_1 = n
    while n>=2:
        n = n >> 1
        i+=1
    i_1 = 2**i
    i_2 = 2**(i+1)
    if n_1-i_1>i_2-n_1:
        return i_2
    else:
        return i_1
