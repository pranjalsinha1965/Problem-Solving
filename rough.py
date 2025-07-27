from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
class ListNode: 
    def __init__(self, val = 0, next = None): 
        self.val = val 
        self.next = next 

class Solution: 
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode: 
        dummy = ListNode(0, head)
        left = dummy 
        right = head 
        
        while n > 0 and right: 
            right = right.next 
            n -= 1 
        
        while right: 
            left = left.next 
            right = right.next 
            
        left.next = left.next.next
        return dummy.next 
    
class Solution: 
    def lengthOfSubstring(self, s: str) -> int: 
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res 
    
class Solution: 
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1 
            l += 1
        res = max(res, r - l + 1)
        return res 
    
# Palindromic Substrings - Leetcode 647 - Python
# Done 
class Solution:
    def countSubstrings(self, s: str) -> int: 
        for i in range(len(s)): 
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res 
        
    def countPali(self, s, l, r): 
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]: 
            res += l
            l -= 1 
            r += 1
        return res 