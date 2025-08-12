from typing import List 
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r: 
        i = l + (r - l)  // 2
        n = nums[i]
        if target > n: 
            l = i + 1   
        elif target < n: 
            r = i - 1 
        else:    
            return 1
    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9 

result = search(nums, target)
print(result)

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
    
def count_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else: 
            frequency[num] = 1
    return frequency

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequency_count = count_frequency(nums)
print(frequency_count)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True 

# Test the function 
num = 17
if is_prime(num):
    print(f"{num} is a prime number")
else:    
    print(f"{num} is not a prime number")

def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item) 
    return common_elements 

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common_elements(list_a, list_b)
print(common)

def bubble_sort(elements):
    n = len(elements)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]

# Test the function
nums = [5, 2, 8, 1, 9]
bubble_sort(nums)
print(nums)

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

nums = [10, 5, 8, 20, 3]
second_largest_num = find_second_largest(nums)
print(f"The second largest number is {second_largest_num}")

def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
unique_nums = remove_duplicates(nums)
print(f"{unique_nums}")

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