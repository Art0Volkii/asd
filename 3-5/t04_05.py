import math

def f(x):
    '''
    Функція f(x) на відрізку [1.6 , 3] незростаюча. 
    '''
    return math.sin(x) - (x / 3)

def binary_search(a,b):
    l = a
    r = b
    eps = 1e-10
    while r - l > eps:
        m = (l + r) / 2.0
        if f(m) > 0:
            l = m
        else:
            r = m
    return (l + r) / 2

x = binary_search(1.6, 3)
print(f"{x:.9f}")
