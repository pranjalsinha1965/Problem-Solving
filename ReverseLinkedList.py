# Definition for single - Linked list...
# class ListNode:
def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def reverseList(self, head):
        p = None
        c = head
        while c:
            tmp = c.next
            c.next = p
            p = c
            c = tmp
        return p

