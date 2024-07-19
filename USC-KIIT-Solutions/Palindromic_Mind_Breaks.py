# MINDBREAKER- PALINDROMIC MATRIX PATHS:
  
# --------------UNIQUE PATHS
def paths(m, n):
    row = [1] * n
    print(row)
    for i in range(m-1):
        newRow = [1] * n
        for j in range(n-2, -1, -1):
            newRow[j] = newRow[j+1] + row[j]
        row = newRow
    return row[0]

print(paths(3, 3))


# THE PATHS
# aaaa (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2)
# aaba (0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (2, 2)
# aabb (0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (2, 2)
# abba (0, 0) -> (1, 0) -> (2, 0) -> (2, 1) -> (2, 2)

# [(0, 1), (0, 2), (1, 1), (1, 2)]
# 0, 0, 3, 2