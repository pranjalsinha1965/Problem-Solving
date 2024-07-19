class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

# Convert Python list to linked list
a = [1, 2, 3, 4, 5]
linked_list = list_to_linked_list(a)

# Reverse the linked list
reversed_linked_list = reverse_list(linked_list)

# Convert reversed linked list back to Python list
b = linked_list_to_list(reversed_linked_list)
print(b)


