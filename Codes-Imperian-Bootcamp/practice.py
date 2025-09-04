from typing import List 
class Solution: 
    def lengthOfLIS(self, nums: List[int]) -> int: 
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1): 
            for j in range(i + 1, len(nums)): 
                if  nums[i ] < nums[j]: 
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
    
# Climbing Stairs → LeetCode 70: Climbing Stairs
# Container With Most Water → LeetCode 11: Container With Most Water
# House Robber → LeetCode 198: House Robber
# House Robber II → LeetCode 213: House Robber II
# Unique Paths → LeetCode 62: Unique Paths
# Jump Game → LeetCode 55: Jump Game
# Cycle Detection → LeetCode 141: Linked List Cycle
# Linked List Reversal → LeetCode 206: Reverse Linked List
# Length of LIS → LeetCode 300: Longest Increasing Subsequence
# Merge Intervals → LeetCode 56: Merge Intervals
# Two Sum → LeetCode 1: Two Sum
# Combination Sum → LeetCode 39: Combination Sum
# Coin Change → LeetCode 322: Coin Change
# Longest Common Subsequence → LeetCode 1143: Longest Common Subsequence
# Word Break → LeetCode 139: Word Break
# Remove Nth Node From End of List → LeetCode 19: Remove Nth Node From End of List
# Longest Substring Without Repeating Characters → LeetCode 3: Longest Substring Without Repeating Characters
# Longest Repeating Character Replacement → LeetCode 424: Longest Repeating Character Replacement
# Palindromic Substrings → LeetCode 647: Palindromic Substrings
# Best Time to Buy and Sell Stock → LeetCode 121: Best Time to Buy and Sell Stock
# Binary Search → LeetCode 704: Binary Search
# Happy Number → LeetCode 202: Happy Number
# Lemonade Change → LeetCode 860: Lemonade Change
# Length of Linked List (not an official LeetCode, but a classic basic Linked List problem, often appears as utility in interviews).
# Merge Two Sorted Lists → LeetCode 21: Merge Two Sorted Lists