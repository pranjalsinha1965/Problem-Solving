class Solution:
    def minimization(self, expression: str) -> str:
        left, right = expression.split('+')
        smallest = float('inf')
        smallestFive = f'(${expression})'