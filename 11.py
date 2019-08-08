class TrieNode:
    def __init__(self, value=""):
        self.value = value
        self.children = dict()
        self.endWord = False

class Trie(TrieNode):
    def add_word(self, word):
        def add_word_helper(node, str):
            if str[0] not in node.children:
                node.children[str[0]] = TrieNode(str[0])
                if len(str) == 1:
                    node.children[str[0]].endWord = True
            if len(str) > 1:
                add_word_helper(node.children[str[0]], str[1:])
        add_word_helper(self, word)

    def predict_word(self, str):
        def get_remaining_tree(str, tree):
            node = tree
            while len(str) > 0:
                if str[0] in node.children:
                    node = node.children[str[0]]
                    str = str[1:]
                else:
                    return None
            return node

        allWords = []
        def all_words_helper(stringSoFar, tree):
            for k in tree.children:
                child = tree.children[k]
                newString = stringSoFar + child.value
                if child.endWord:
                    allWords.append(newString)
                all_words_helper(newString, child)

        remainingTree = get_remaining_tree(str, self)
        if remainingTree is not None:
            all_words_helper(str, remainingTree)

        return allWords
    def log_all(self):
        print(self.predict_word(""))

options = ["dog", "deer", "deal", "degree", "degrau"]

trie = Trie()
for option in options:
    trie.add_word(option)
#trie.log_all()
print(trie.predict_word("deg"))