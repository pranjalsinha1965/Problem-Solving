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

from typing import List 
class Solution: 
    def combinationSums(self, candidates: List[int], target: int) -> List[List[int]]: 
        res = []

        def dfs(i, cur, total): 
            if total == target: 
                res.append(cur.copy())
                return 
            if i >= len(candidates) or total > target: 
                return 
            cur.append(candidates[i])
            cur.pop()
            dfs(i, cur, total + candidates[i])
        
        dfs(0, [], 0)
        return res 
    
my_solution = Solution()
candidates = [2, 3, 6, 7]
target = 7 
print(my_solution.combinationSums(candidates, target))



    

    


    
    

    


        




