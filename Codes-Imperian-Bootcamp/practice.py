# TwoSum 
# Container with most water 
# Best time to buy and sell stocks 
# Clone Graph - Depth First Search - Leetcode 133 
# Rotate Image - Leetcode 
# Valid Parenthesis 
# Binary Search 
# Length of Longest Increasing Subsequence 
# climbStairs 
# House Robbery I 
# House Robbery II 
# unique Paths 
# CanJump 
# isHappy 

def count_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency: 
            frequency[num] += 1
        else: 
            frequency[num] = 1 
    return frequency

def is_prime(number):
    if number < 2: 
        return False 
    for i in range(2, int(number**0.5) + 1): 
        if number % i == 0:
            return False 
    return True 

