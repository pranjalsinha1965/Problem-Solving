# INSERTION SORT - SWAPPING ELEMENTS
A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
def swap(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break
    return A
print(swap(A))