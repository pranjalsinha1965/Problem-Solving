def moveZeros(n,  a):
    # Temporary array
    temp = []
    # Copy non-zero elements from original to temp array
    for i in range(n):
        if a[i] != 0:
            temp.append(a[i])
    # Number of non-zero elements
    nz = len(temp)
    # Copy elements from temp to fill first nz fields of original array
    for i in range(nz):
        a[i] = temp[i]
    # Fill the rest of the cells with 0
    for i in range(nz, n):
        a[i] = 0
    return a
arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = 10
ans = moveZeros(n, arr)
for it in ans:
    print(it, end=" ")
print()



