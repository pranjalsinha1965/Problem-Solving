class Solution: 
    def climbStairs(self, n: int) -> int: 
        one, two = 1, 1
        for i in range(n - 1): 
            temp = one 
            one = one + two 
            two = temp 
        return one  # Return 'one' instead of 'two' to get correct result
    
my_solution = Solution()
n = 5
print(my_solution.climbStairs(n))  # Output: 8

def maxArea(heights: List[int]) -> int:
    l, r = 0, len(heights) - 1 
    res = 0  # Initialize the result variable
    while l < r:
        res = max(res, min(heights[l], heights[r]) * (r - l))
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
            
    return res

heights = [1,8,6,2,5,4,8,3,7]
print(maxArea(heights)) 

class Solution: 
    def rob(self, nums: List[int]) -> int: 
        rob1, rob2 = 0, 0
        for n in nums: 
            temp = max(n + rob1, rob2)
            rob1 = rob2 
            rob2 = temp 
        return rob2 
    
class Solution: 
    def rob(self, nums: List[int]) ->int: 
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums): 
        rob1, rob2 = 0, 0
        for n in nums: 
            newRob = max(rob1 + n, rob2)
            rob1 = rob2 
            rob2 = newRob 
        
        return rob2 

#one 
class Solution: 
    def uniquePaths(self, m: int, n: int) -> int: 
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1): 
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row 

#two
class Solution: 
    def canJump(self, nums: List[int]) ->bool: 
        goal = len(nums) - 1 
        for i in range(len(nums) -1, -1, -1): 
            if i + nums[i] >= goal: 
                goal = i 
        
        return True if goal == 0 else False 

#three    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#four
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

#five
class Solution: 
    def lengthOfLIS(self, nums: List[int]) -> int: 
        LIS = [1] * len(nums)
        
        # Traverse the list from right to left
        for i in range(len(nums) - 1, -1, -1): 
            for j in range(i + 1, len(nums)): 
                if nums[i] < nums[j]:  
                    LIS[i] = max(LIS[i], 1 + LIS[j])  
        return max(LIS)

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