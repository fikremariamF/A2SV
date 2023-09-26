class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            idx = ord(letter) - ord("a")
            if curr.children[idx]:
                curr = curr.children[idx]
            else:
                node = TrieNode()
                curr.children[idx] = node
                curr = node
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            idx = ord(letter) - ord("a")
            if curr.children[idx]:
                curr = curr.children[idx]
            else:
                return False
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            idx = ord(letter) - ord("a")
            if curr.children[idx]:
                curr = curr.children[idx]
            else:
                return False
        return True
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end_of_word = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)