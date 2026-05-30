class TrieNode:
    def __init__(self, val, term):
        self.children = {}
        self.value = val
        self.terminal = term

class PrefixTree:

    def __init__(self):
        self.root = TrieNode('', False)

    def insert(self, word: str) -> None:
        print('insert')
        ptr = self.root
        for i in range(len(word)-1):
            if word[i] not in ptr.children:
                ptr.children[word[i]] = TrieNode(word[i], False)
            ptr = ptr.children[word[i]]
            print(ptr.value, ptr.terminal)
        if word[len(word)-1] not in ptr.children:
            ptr.children[word[len(word)-1]] = TrieNode(word[len(word)-1], True)
        else:
            ptr.children[word[len(word)-1]].terminal = True
        ptr = ptr.children[word[len(word)-1]]
        print(ptr.value, ptr.terminal)
        print("\n")
        return

    def search(self, word: str) -> bool:
        print('search')
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
            print(ptr.value)
            print(ptr.terminal)
        print(ptr.children)
        return ptr.terminal

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return True
        