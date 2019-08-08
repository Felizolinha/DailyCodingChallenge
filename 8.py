class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_unival(root):
    if root.left is None and root.right is None:
        return True
    elif is_unival(root.left) and is_unival(root.right) and root.left.val == root.right.val:
        return True
    else:
        return False

def count_unival_subtrees(root):
    left_count = count_unival_subtrees(root.left) if root.left is not None else 0
    right_count = count_unival_subtrees(root.right) if root.right is not None else 0
    if is_unival(root):
        return left_count+right_count+1
    else:
        return left_count+right_count

tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print(count_unival_subtrees(tree))