def karacuba_mul(A, B):

    n, m = len(A), len(B)
    res = [0] * (n + m) 

    A = [int(d) for d in A][::-1]
    B = [int(d) for d in B][::-1]

    for i in range(n):
        for j in range(m):
            res[i + j] += A[i] * B[j]
            res[i + j + 1] += res[i + j] // 10
            res[i + j] %= 10

    while len(res) > 1 and res[-1] == 0:
        res.pop()

    return ''.join(map(str, res[::-1]))  

A, B = input().split()

print(karacuba_mul(A, B))

#RES: 20%
