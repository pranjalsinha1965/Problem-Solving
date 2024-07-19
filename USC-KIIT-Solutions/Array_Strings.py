def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

a = [1, 2, 3, 4, 5]
b = two_sum(a, 5)

print(b)

# prints the index at which required sum is present



