def qsort(array, a, b):
    if a >= b: return

    pivot = array[a + (b - a) // 2]
    left = a ; right = b  

    while True:
        while array[left] < pivot:  
            left += 1  

        while array[right] > pivot:  
            right -= 1  

        if left >= right:  
            break  

        array[left], array[right] = array[right], array[left]  
        left += 1  
        right -= 1  

    qsort(array, a, right)  
    qsort(array, right + 1, b)  

n = int(input())  
numbers = list(map(int, input().split()))  

qsort(numbers, 0, n - 1)  

print(*numbers)
