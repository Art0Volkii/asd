import sys

def fun(ind, res):
    global max_sum

    if res > N:
        return
    
    if res in memory and memory[res] >= ind:
        return 

    memory[res] = ind

    if res > max_sum:
        max_sum = res

    if ind < s:
        fun(ind + 1, res + tracks[ind]) 
        fun(ind + 1, res)

lines = sys.stdin.read().splitlines()

for line in lines:
    data = list(map(int, line.split()))
    N, s = data[0], data[1]
    tracks = data[2:]
    
    max_sum = 0
    memory = {}

    fun(0, 0)
    
    print(f"sum:{max_sum}")

#RES: 100%
