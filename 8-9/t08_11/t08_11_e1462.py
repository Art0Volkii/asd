def selection_sort(n, array):

    for i in range(n - 1, 0, -1):
        maxpos = 0
        for j in range(1, i + 1):
            max_dig = array[maxpos] % 10
            j_dig = array[j] % 10

            if (j_dig > max_dig or
                (j_dig == max_dig and array[j] > array[maxpos])):
                maxpos = j

        array[i], array[maxpos] = array[maxpos], array[i]
    return array

n = int(input())
numbers = [int(input().strip()) for _ in range(n)]

print(" ".join(map(str, selection_sort(n, numbers))))
