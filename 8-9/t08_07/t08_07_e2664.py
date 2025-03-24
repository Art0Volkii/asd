n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    curr_val = arr[i]
    poss = i

    while poss > 0:
        if arr[poss - 1] > curr_val:
            arr[poss] = arr[poss - 1]
            poss -= 1
        else: break

    if poss != i:  
        arr[poss] = curr_val
        print(" ".join(map(str, arr)))
    else:
        arr[poss] = curr_val
