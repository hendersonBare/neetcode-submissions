class TrieNode():
    def __init__(self, value: str, term: bool):
        self.val = value
        self.children = {}
        self.terminal = term

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("", False)

    def addWord(self, word: str) -> None:
        ptr = self.root
        for i in range(len(word)-1):
            if word[i] not in ptr.children:
                ptr.children[word[i]] = TrieNode(word[i], False)
            ptr=ptr.children[word[i]]
        last = word[len(word)-1]
        if last not in ptr.children:
            ptr.children[last] = TrieNode(last, True)
        ptr.children[last].terminal = True
        return

    def search(self, word: str) -> bool:
        def helperSearch(node, word):
            print(word)
            if len(word) == 0:
                return node.terminal
            ptr = node
            for i in range(len(word)):
                if word[i] == ".":
                    for child in ptr.children.values():
                        if (helperSearch(child, word[i+1:])):
                            return True
                    return False
                else:
                    if word[i] not in ptr.children:
                        return False
                    ptr = ptr.children[word[i]]
            return ptr.terminal


        return helperSearch(self.root, word)
