def gcf(a, b):
    if a<b:
        a, b =b, a
    while True:
        c = a%b
        if c == 0:
            return b
            break
        a = b
        b = c
    return None

if __name == '__main__':
    a = 50
    b = 15
    print(gcf(a, b))
