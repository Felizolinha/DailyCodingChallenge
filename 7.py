class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def calculate_node(remaining):
    root = Node(remaining)
    remaining2 = remaining[:2]
    if len(remaining) > 0:
        root.left = calculate_node(remaining[1:])
    if len(remaining2) == 2 and int(remaining2) <= 26:
        root.right = calculate_node(remaining[2:])
    return root

def count_leaves(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return count_leaves(root.left) + count_leaves(root.right)

testCase = '221282229182918928192912195211191212192819813'
print(count_leaves(calculate_node(testCase)))