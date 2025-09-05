# Test - 1 Solutions

from typing import List 

class Solution: 
    def twoSum(self, numbers: List[int], target: int) -> int: 
        l, r = 0, len(numbers) - 1
        while l < r: 
            curSum = numbers[l] + numbers[r]
            if curSum > target: 
                r -= 1 
            elif curSum < target: 
                l += 1
            else: 
                return [l + 1, r - 1]
        return []
    
nums = [2, 3, 4, 5]
result = 8

my_solution = Solution()
answer = my_solution.twoSum(nums, result)


print(f"Given list off integers is: {nums}")
print(f"The target result is: {result}")
print(f"Thus the answer is: {answer}")

def maxArea(heights: List[int]) -> int: 
    l, r = 0, len(heights) - 1
    res = 0
    while l < r: 
        res = max(res, min(heights[l], heights[r]) * (r - l))
        if heights[l] < heights[r]: 
            l += 1
        else:
            r -= 1 
    return res 

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(heights))

def maxProfit(prices: List[int]) -> int: 
    buy = prices[0]
    profit = 0
    for p in prices:
        buy = min(buy, p)
        profit = max(profit, p - buy)
    return profit 

prices = [7, 1, 5, 3, 6, 4]
result = maxProfit(prices)
print(f"Maximum Profit: {result}")

def canJump(self, nums: List[int]) -> int: 
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal: 
            goal = i 

    return True if goal == 0 else False 

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

customers = [5, 5, 5, 10, 20]
result = lemonadeChange(None, customers)
print(result)

def search(nums: List[int], target: int) -> int: 
    l, r = 0, len(nums) - 1
    while l < r: 
        i = l + (r - l) // 2
        n = len(nums)
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

class ListNode: 
    def __init__(self, val = 0, next = None): 
        self.val = val
        self.next = next 

class Solution: 
    def hasCycle(self, head: ListNode): 
        slow, fast = head, head 
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 
            if slow == fast: 
                return True 
        return True 
    
class Solution: 
    def reverseList(self, head:ListNode) -> ListNode: 
        if not head or not head.next: 
            return head 
        newHead = self.reverseList(head.next)
        head.next.next = head 
        head.next = None 
        return newHead 

class Solution: 
    def removeNthFromEnd(self, head:ListNode, n: int) -> ListNode: 
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
    def lengthOfLIS(nums: List[int]) -> int: 
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1): 
            for j in range(i + 1, len(nums)): 
                if nums[i] < nums[j]: 
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
    
nums = [1, 2, 4, 5]
result = Solution.lengthOfLIS(nums)
print(f"The length of the longest increasing subsequence is: {result}")

def climbStairs(n: List[int]) -> int: 
    one, two = 1, 1
    for i in range(n - 1): 
        temp = one 
        one = one + two 
        two = temp 
    return one 

n = 5 
print(climbStairs(n))

def rob(self, nums: List[int]) -> int: 
    rob1, rob2 = 0, 0 
    for n in nums: 
        temp = max(n + rob1, rob2)
        rob1 = rob2 
        rob2 = temp 
    return rob2 

def rob(self, nums: List[int]) -> int:
    return max(nums[0], self.helper(nums[1:]), self.helper(nums[:0]))

def helper(self, nums: List[int]) -> int: 
    rob1, rob2 = 0, 0 
    for n in nums: 
        temp = max(n + rob1, rob2)
        rob1 = rob2 
        rob2 = temp 
    return rob2 

def unique_paths(self, m: int, n: int) -> int: 
    row = [1] * n 
    for i in range(m - 1): 
        newRow = [1] * n 
        for j in range(n - 2, -1, -1): 
            newRow[j] = newRow[j + 1] + row[j]
        row = newRow 
    return row 

class Solution: 
    def coinChange(self, coins: List[int], amount: int) -> int: 
        self.result = float('-inf')

        def dfs(remaining_amount, count): 
            if remaining_amount == 0: 
                self.result = min(self.result, count)
                return 
            if remaining_amount < 0: 
                return 
            for coin in coins: 
                dfs(remaining_amount - count, count + 1)
        dfs(amount, 0)
        return self.result if self.result != float('-inf') else -1 
    
coins = [1, 3, 4, 5]
amount = 7 
my_solution = Solution()
print(my_solution.coinChange(coins, amount))


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
candidates = [2, 3, 4, 5, 7]
target = 7 
print(my_solution.combinationSum(candidates, target))

def lengthOfLIS(nums: List[int]) -> int: 
    LIS = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)): 
            if nums[i] < nums[j]: 
                LIS[i] = max(LIS[i], LIS[j] + 1)
    return max(LIS)

nums = [1, 2, 4, 3]
result = lengthOfLIS(nums)
print(f"The length of the longest increasing subsequence us: {result}")

class Solution: 
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1): 
            for j in range(len(text2)-1, -1, -1): 
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else: 
                    dp[i][j] = max(dp[i][j + 1], dp[i+1][j])
        
        return dp[0][0]
    
Solution = Solution()
text1 = "abcde"
text2 = "ace"
result = Solution.longestCommonSubsequence(text1, text2)
print(result)

class Solution: 
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        dp = [False] * (len(s) + 1)
        for i in range(len(s) - 1, -1, -1): 
            for w in wordDict: 
                if (i + len(w)) < len(s) and s[i: i + len(w)] == w: 
                    dp[i] = dp[i + len(w)]
                if dp[i]: 
                    break 
        return dp[0]
    

solution = Solution()
s = "leetcode"
wordDict = ["leet", "code"]
print(solution.wordBreak(s, wordDict))

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
    def charactersReplacement(self, s: str, k : int) -> int: 
        count = ()
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
            res += 1
        return res 
    
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
    