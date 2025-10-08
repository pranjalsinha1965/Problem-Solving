from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda i: i[0])

        # Step 2: Initialize output with the first interval
        output = [intervals[0]]

        # Step 3: Merge overlapping intervals
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:  # overlap case
                output[-1][1] = max(lastEnd, end)
            else:  # no overlap → append
                output.append([start, end])

        return output


# Create an object of Solution
solution = Solution()
print(solution.merge([[1, 3], [2, 4], [5, 7], [6, 8]]))
