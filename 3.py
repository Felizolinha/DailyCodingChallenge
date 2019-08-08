class RefString:
    def __init__(self, s):
        self.s = s

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root, s):
    if root is None:
        s.s += "* "
        return
    s.s += root.val + " "
    serialize(root.left, s)
    serialize(root.right, s)

def readValue(refStr):
    result = ""
    i=0
    while(i<len(refStr.s) and refStr.s[i] is not " "):
        result += refStr.s[i]
        i += 1
    refStr.s = refStr.s[i+1:]
    return result

def deserialize(root, refString):
    value = readValue(refString)
    if(value is "*"):
        return

    root = Node(value)
    root.left = deserialize(root.left, refString)
    root.right = deserialize(root.right, refString)
    return root

teste=RefString("")
node = Node('root', Node('left', Node('left.left')), Node('right'))
serialize(node, teste)
#print(teste.s)
deserializedNode = deserialize(None, teste)
print(deserializedNode.left.left.val)
assert deserializedNode.left.left.val == 'left.left'
