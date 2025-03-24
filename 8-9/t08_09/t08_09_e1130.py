def sum_of_digits(x):
    return sum(int(digit) for digit in str(x))

def insertion_sort(n, array):
    for i in range(1, n):
        curr_val = array[i]
        poss = i

        while poss > 0:
            if (sum_of_digits(array[poss - 1]) > sum_of_digits(curr_val) or
                (sum_of_digits(array[poss - 1]) == sum_of_digits(curr_val) and str(array[poss - 1]) > str(curr_val))):
                array[poss] = array[poss - 1]
                poss -= 1
            else:
                break
        array[poss] = curr_val


n = int(input())
k = int(input()) 

numbers = list(range(1, n + 1))

insertion_sort(n, numbers)

index_k = numbers.index(k) + 1

print(index_k)
print(numbers[k - 1])
