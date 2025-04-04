def get_permutations(n, k, curr_perm, used):
    if len(curr_perm) == k:
        print(" ".join(map(str, curr_perm)))
        return

    for i in range(1, n + 1):
        if not used[i]:

            used[i] = True
            curr_perm.append(i)
            get_permutations(n, k, curr_perm, used)
            curr_perm.pop()
            used[i] = False

n, k = map(int, input().split())

get_permutations(n, k, [], [False] * (n + 1))

#RES: 100%
