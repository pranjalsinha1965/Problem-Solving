from typing import List
# Corrected function without 'self'
def maxProfit(prices: List[int]) -> int: 
    profit = 0
    buy = prices[0]

    for p in prices: 
        buy = min(buy, p)
        profit = max(profit, p - buy)
    return profit 

prices = [7, 1, 5, 3, 6, 4]  # Example input
result = maxProfit(prices)   
print(f"Maximum Profit: {result}")

from typing import List

def search(nums: List[int], target: int) -> int:  
    l, r = 0, len(nums) - 1 
    while l <= r:  
        i = l + (r - l) // 2  # Calculate the middle index
        n = nums[i]  # Get the middle element
        if target > n:  
            l = i + 1  
        elif target < n:  
            r = i - 1
        else:
            return i 
    return -1  

nums = [-1, 0, 3, 5, 9, 12]
target = 9

result = search(nums, target)
print(result)  

class Solution: 
    def isHappy(n: int) -> bool: 
        def sum_of_squares(n): 
            res = 0
            while n: 
                res += (n % 10) ** 2
                n = n // 10
            return res 
        
        slow, fast = n, sum_of_squares(n)
        while slow != fast: 
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
        return True if slow == 1 else False 

#Eating fresh lemonade change
from typing import List

def lemonadeChange(self, bills: List[int]) -> bool:
    five, ten = 0, 0
    
    for b in bills:
        if b == 5:
            five += 1
        elif b == 10:
            if five > 0:
                five -= 1
                ten += 1
            else:
                return False
        elif b == 20:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    
    return True

# Example Usage
customers = [5, 5, 5, 10, 20]
result = lemonadeChange(None, customers)
print(result)

# Container with most water
# Done

from typing import List

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

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: 
        l, r = 0, len(numbers) - 1 
        
        while l < r:
            curSum = numbers[l] + numbers[r]  # Calculate current sum
            
            if curSum > target:
                r -= 1  
            elif curSum < target:
                l += 1  
            else:
                return [l + 1, r + 1]  
        return [] 
    
nums = [2, 3, 4, 5]
result = 8

my_solution = Solution()
answer = my_solution.twoSum(nums, result)

print(f"Given list of numbers is {nums}")
print(f"The target result is {result}")
print(f"Thus, the answer is {answer}")  

# Combination Sum - Backtracking
from typing import List 

class Solution: 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: 
        res = []
        
        def dfs(i, cur, total): 
            if total == target: 
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target: 
                return 
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res 

my_solution = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(my_solution.combinationSum(candidates, target))

# climbstairs solution
# Done 
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

## House Robber - Leetcode 198 - Python Dynamic Programming
# Done 
class Solution: 
    def rob(self, nums: List[int]) -> int: 
        rob1, rob2 = 0, 0
        for n in nums: 
            temp = max(n + rob1, rob2)
            rob1 = rob2 
            rob2 = temp 
        return rob2 
    
## House Robber II - Dynamic Programming - Leetcode 213
# Done 
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

## Unique Paths - Dynamic Programming - Leetcode 62
# Done 
class Solution: 
    def uniquePaths(self, m: int, n: int) -> int: 
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1): 
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row 
    
## Jump Game - DP - Greedy - Leetcode 55
# Done 
class Solution: 
    def canJump(self, nums: List[int]) ->bool: 
        goal = len(nums) - 1 
        for i in range(len(nums) -1, -1, -1): 
            if i + nums[i] >= goal: 
                goal = i 
        
        return True if goal == 0 else False 
    