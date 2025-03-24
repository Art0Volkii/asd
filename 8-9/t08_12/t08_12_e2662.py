def selection_sort(n, array):
    f_ind = 0
    counter = 0

    for i in range(n - 1):
        min_poss = i 

        for j in range(i + 1, n):
            if array[j] < array[min_poss]:
                min_poss = j

        array[i], array[min_poss] = array[min_poss], array[i]

        if f_ind == i:
            f_ind = min_poss
        elif f_ind == min_poss:
            f_ind = i

        if f_ind != 0:
            counter += 1  

    return counter

n = int(input())  
numbers = list(map(int, input().split()))  

print(selection_sort(n, numbers))
