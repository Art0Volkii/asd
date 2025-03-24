def select_sort(n, array):
    for i in range(n-1, 0, -1):
        max_ind = 0
        for j in range(1, i+1):
            if array[max_ind] < array[j]:
                max_ind = j
            array[i], array[max_ind] = array[max_ind], array[i]
    return array

n = int(input())
array = [input() for _ in range(n)]

print("\n".join(select_sort(n, array)))

#RES: 100%
