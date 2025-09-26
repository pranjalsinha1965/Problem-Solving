from typing import List

class Solution: 
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)): 
            # Case 1: newInterval ends before current interval starts
            if newInterval[1] < intervals[i][0]: 
                res.append(newInterval)
                return res + intervals[i:]   # append remaining intervals

            # Case 2: newInterval starts after current interval ends
            elif newInterval[0] > intervals[i][1]: 
                res.append(intervals[i])

            # Case 3: Overlapping intervals → merge them
            else: 
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]
        
        res.append(newInterval)  # append merged interval if not added
        return res

solution = Solution()

print(solution.insert([[1,3],[6,9]], [2,5]))  
# Expected: [[1,5],[6,9]]

print(solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  
# Expected: [[1,2],[3,10],[12,16]]

print(solution.insert([], [5,7]))  
# Expected: [[5,7]]

print(solution.insert([[1,5]], [2,3]))  
# Expected: [[1,5]]

print(solution.insert([[1,5]], [2,7]))  
# Expected: [[1,7]]
