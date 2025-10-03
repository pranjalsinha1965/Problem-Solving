class Solution: 
    def isValid(Self, s: str) -> bool: 
        stack = []
        closeToOpen = {
            ')' : '(', 
            '}' : '{', 
            ']' : '['
        }