def bubble_by_class(n, array):
    for i in range(1, n):
        for j in range(1, n - i + 1):
            if (array[j - 1][0] > array[j][0] or
                (array[j - 1][0] == array[j][0] and array[j - 1][1] > array[j][1])):
                array[j - 1], array[j] = array[j], array[j - 1]

def bubble_by_name(n, array):
    for i in range(1, n):
        for j in range(1, n - i + 1):
            if (array[j - 1][0] == array[j][0] and array[j - 1][1] == array[j][1]):
                if (array[j - 1][2] > array[j][2] or
                    (array[j - 1][2] == array[j][2] and array[j - 1][3] > array[j][3])):
                    array[j - 1], array[j] = array[j], array[j - 1]
                  
n = int(input())

students = []

for _ in range(n):
    last_n = input()
    first_n = input()
    clas = input()
    birth = input()

    clas_n = int(clas[:-1])
    clas_l = clas[-1]

    students.append((clas_n, clas_l, last_n, first_n, birth))

bubble_by_class(n, students)

bubble_by_name(n, students)

for student in students:
    class_full = f"{student[0]}{student[1]}"
    print(class_full, student[2], student[3], student[4])
