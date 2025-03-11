def f(x):
    '''
    Функція f(x) на відрізку [0, 2] дуже швидко зростаюча.
    '''
    return x**3 + 4*x**2 + x - 6

def binary_search(a,b):
    l = a
    r = b
    eps = 1e-9
    while abs(r - l) > eps:
        m = (l + r) / 2.0
        if f(m) < 0:
            l = m
        else:
            r = m
    return (l + r) / 2

x = binary_search(0, 2)
print(f"{x:.9f}")

#RES:  1.000000000
