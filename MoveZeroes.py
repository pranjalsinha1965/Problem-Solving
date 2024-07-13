from typing import List
def moveZeroes(self, nums: List[int]) -> None:
    snakeSize = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            snakeSize += 1
        else:
            tmp = nums[i]
            nums[i] = nums[i-snakeSize]
            nums[i - snakeSize] = tmp
        