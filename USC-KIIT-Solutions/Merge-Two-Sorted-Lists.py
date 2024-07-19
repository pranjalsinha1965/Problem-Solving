class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

def list_to_linked_list(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
l1 = list_to_linked_list(a)
l2 = list_to_linked_list(b)
merged = merge_two_lists(l1, l2)
merged_list = linked_list_to_list(merged)
print(merged_list)

