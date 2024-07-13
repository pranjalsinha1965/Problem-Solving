from typing import List
class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        num_to_i = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_to_i:
                return i, num_to_i[comp]
            num_to_i[num] = i

#T: O(n), S: O(n)

