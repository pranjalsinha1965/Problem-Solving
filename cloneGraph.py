class Node: 
    def __init__(self, val=0, neighbours=None): 
        self.val = val
        self.neighbours = neighbours if neighbours is not None else []

class Solution: 
    def cloneGraph(self, node: 'Node') -> 'Node': 
        if not node: 
            return None 
        oldToNew = {}
        def dfs(node): 
            if node in oldToNew: 
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy 
            for nei in node.neighbours: 
                copy.neighbours.append(dfs(nei))
            return copy
        return dfs(node)

# Test case
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbours = [node2, node4]
node2.neighbours = [node1, node3]
node3.neighbours = [node2, node4]
node4.neighbours = [node1, node3]

solution = Solution()
clone_graph = solution.cloneGraph(node2)

print("Original Node: ", node1.val)
print("Cloned Node: ", clone_graph.val)
