def binary_search(array, x, flag):
    l = 0
    r = len(array)
    while l < r:
        m = (l + r) // 2
        if array[m] < x or (flag and array[m] == x):
            l = m + 1
        else:
            r = m
    return l

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
nums = list(map(int, input().split()))

for num in nums:
    left = binary_search(arr, num, False)
    right = binary_search(arr, num, True)
    print(right - left)
