from typing import List
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    unique = set(nums1)
    ans = set()
    for num in nums2:
        if num in unique and num not in ans:
            ans.add(num)
    return ans

