# INSERTION SORT - SHIFTING ELEMENTS
A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
def insert_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

A = [5, 2, 4, 6, 1, 3]
print(insert_sort(A))