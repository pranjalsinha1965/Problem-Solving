class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_level_order(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        # Insert left child
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # Insert right child
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right

# List representation of the tree
a = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

# Create the binary tree from the list
root = insert_level_order(a, None, 0, len(a))

# Find nodes p and q
p = find_node(root, 5)
q = find_node(root, 1)

# Find the lowest common ancestor
lca = lowest_common_ancestor(root, p, q)
print(lca.val if lca else None)
