options = ["dog", "deer", "deal"]

class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = dict()
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        if node.name not in self.children:
            self.children[node.name] = Tree(name=node.name)
    def follow(self, path):
        result = self.children
        for p in path:
            if p in result:
                result = result[p].children
            else:
                result = None
                break


'''
def convert_list_to_tree(options):
    root = Tree()
    for option in options:
        optionTree = Tree()
        for i in option:
            optionTree.name = l
            optionTree.add
'''