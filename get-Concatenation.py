from typing import List
def getConcatenation(self, nums: List[int], x: int) -> List[int]:
    ans = []
    for _ in range(x):
        for num in nums:
            ans.append(num)
        
        return ans
    
