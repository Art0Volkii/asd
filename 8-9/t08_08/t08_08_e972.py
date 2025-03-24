def bubble_sort(n, array):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:  
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


n = int(input())

array = []  
for _ in range(n):  
    hours, minutes, seconds = map(int, input().split()) 
    array.append((hours, minutes, seconds))

for time in bubble_sort(n, array):
    print(*time) 
