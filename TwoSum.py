# from typing import List
# def twoSum(self, nums, target):
#     nums.sort()
#     l, r = 0, len(nums) - 1
#     while l<r: 
#         tot = nums[l] + nums[r]
#         if tot == target:
#             return l, r
#         elif tot < target:
#             l += 1
#         else:
#             r -= 1

from typing import List, Tuple
def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return num_to_index[complement], i
        num_to_index[num] = i
    return None

