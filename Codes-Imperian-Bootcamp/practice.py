from typing import List
class Solution: 
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]: 
            lastEnd = output[-1][1]
            if start <= lastEnd: 
                output[-1][1] = max(lastEnd, end)
            else: 
                output.append([start, end])
        return output 
    
intervals = [[8,10],[1,3],[2,6],[15,18]]
intervals.sort(key=lambda i: i[0])
print(intervals)

