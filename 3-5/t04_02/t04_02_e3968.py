def find_x(C):
    l = 0
    r = C 
    eps = 1e-6 

    while r - l > eps:
        m = (l + r) / 2
        if m ** 2 + m ** 0.5 <= C:
            l = m
        else:
            r = m

    return l

C = float(input().strip())
print(f"{find_x(C):.6f}")
