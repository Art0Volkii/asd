def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][0] <= righthalf[j][0]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1

n = int(input())  
robots = [tuple(map(int, input().split())) for _ in range(n)]  

merge_sort(robots)

for robot in robots:
    print(*robot)
