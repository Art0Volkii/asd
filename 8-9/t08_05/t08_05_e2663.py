def bubble_sort(n, arrray):
    num = 0
    for pass_s in range(n - 1, 0, -1):
        for i in range(pass_s):
            if arrray[i] > arrray[i + 1]:
                arrray[i], arrray[i + 1] = arrray[i + 1], arrray[i]
                num+=1
    return num

n = int(input())
arrray = [int(x) for x in input().split()]

print(bubble_sort(n, arrray))

#RES: 100%
