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

## Coin Change: Greedy ? [1, 3, 4, 5] Amount 
# for this use DFS Backtracking 
# [1, 3, 4, 5] Amount = 7

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # To store the minimum number of coins
        self.result = float('inf')

        def dfs(remaining_amount, count):
            if remaining_amount == 0:
                self.result = min(self.result, count)
                return
            if remaining_amount < 0:
                return
            for coin in coins:
                dfs(remaining_amount - coin, count + 1)
        dfs(amount, 0)
        return self.result if self.result != float('inf') else -1

# Example test case:
coins = [1, 3, 4, 5]
amount = 7
my_solution = Solution()
print(my_solution.coinChange(coins, amount))  # Output: 2 (3+4 or 4+3)

## Longest Increasing Subsequence 
## 1st step: Brute - Force - DFS 
## 2nd step: DFS - With Code 
## [1, 2, 4, 3]
# Done 
from typing import List

class Solution: 
    def lengthOfLIS(self, nums: List[int]) -> int: 
        LIS = [1] * len(nums)
        
        # Traverse the list from right to left
        for i in range(len(nums) - 1, -1, -1): 
            for j in range(i + 1, len(nums)): 
                if nums[i] < nums[j]:  # If a smaller element is found at the right of nums[i]
                    LIS[i] = max(LIS[i], 1 + LIS[j])  # Update LIS at i
        return max(LIS)

# Example usage
nums = [1, 2, 4, 3]
result = Solution().lengthOfLIS(nums)
print(f"The length of the longest increasing subsequence is: {result}")  # Expected output: 3

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Initialize the DP table with zeros
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        
        # Fill the DP table from the bottom-right corner
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        # The result is in the top-left cell of the DP table
        return dp[0][0]

# Example usage:
solution = Solution()
text1 = "abcde"
text2 = "ace"
result = solution.longestCommonSubsequence(text1, text2)
print(result)  # Output: 3

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break  # Break if a valid word is found for dp[i]
        return dp[0]

# Test cases
sol = Solution()
# Test case 1
s = "leetcode"
wordDict = ["leet", "code"]
print(sol.wordBreak(s, wordDict))  # Expected: True
# Test case 2
s = "applepenapple"
wordDict = ["apple", "pen"]
print(sol.wordBreak(s, wordDict))  # Expected: True
# Test case 3
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(sol.wordBreak(s, wordDict))  # Expected: False

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
    
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output
    
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
    
class ListNode: 
    def __init__(self, val = 0, next = None): 
        self.val = val 
        self.next = next 

class Solution: 
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode: 
        dummy = ListNode(0, head)
        left = dummy 
        right = head 
        
        while n > 0 and right: 
            right = right.next 
            n -= 1 
        
        while right: 
            left = left.next 
            right = right.next 
            
        left.next = left.next.next
        return dummy.next 
    
class Solution: 
    def lengthOfSubstring(self, s: str) -> int: 
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res 
    
class Solution: 
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1 
            l += 1
        res = max(res, r - l + 1)
        return res 
    
# Palindromic Substrings - Leetcode 647 - Python
# Done 
class Solution:
    def countSubstrings(self, s: str) -> int: 
        for i in range(len(s)): 
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res 
        
    def countPali(self, s, l, r): 
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]: 
            res += l
            l -= 1 
            r += 1
        return res 
    
def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item) 
    return common_elements 

def bubble_sort(elements):
    n = len(elements)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]

def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers
