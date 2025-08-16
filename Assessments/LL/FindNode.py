class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Read the number of test cases, skipping any empty lines
t_line = input().strip()
while t_line == '':
    t_line = input().strip()
t = int(t_line)

for _ in range(t):
    data_line = input().split()
    head = None
    tail = None
    for token in data_line:
        if token == '-1':
            break
        data = int(token)
        new_node = Node(data)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
            
    N_line = input().strip()
    while N_line == '':
        N_line = input().strip()
    N = int(N_line)
    
    current = head
    index = 0
    found_index = -1
    while current is not None:
        if current.data == N:
            found_index = index
            break
        current = current.next
        index += 1
        
    print(found_index)