def binary_search(array, x):
    left = 0
    right = len(array) - 1
    while left <= right:
        m = (left + right) // 2
        if array[m] == x:
            return True
        elif array[m] < x:
            left = m + 1
        else:
            right = m - 1
    return False
n = int(input())
array = list(map(int, input().split()))
m = int(input())
numbs = list(map(int, input().split()))
for numb in numbs:
    if binary_search(array, numb):
        print("YES")
    else:
        print("NO")
