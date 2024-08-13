class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "" or s == t: 
            return True
        
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
                if j == len(s):
                    return True
        return False

# Create an instance of the Solution class
solution = Solution()

# Check if "ababc" is a subsequence of "cabb"
s = solution.isSubsequence("ababc", "cabb")
print(s)  # Output: False
