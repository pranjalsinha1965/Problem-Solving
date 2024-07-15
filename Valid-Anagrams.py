#Return True if string 's' and 't' are anagrams
s = "silent"
t = "listen"
from collections import Counter
class Solutions:
    def isAnagram(self, str, t):
        if len(s) != len(s):
            return False
        charCount = dict(Counter(s))
        for ch in s:
            if ch not in charCount or charCount[ch] == 0:
                return False
            charCount[ch] -= 1
        return True