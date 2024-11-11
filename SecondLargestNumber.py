'''
    Time complexity: O(N * Log(N))
    Space complexity: O(1)

    Where 'N' is the input array 'A'.
'''

from typing import List
def getSecondOrderElements(n,  a):
    # Sorting out the given input array.
    a.sort()
    return [a[n - 2], a[1]]

