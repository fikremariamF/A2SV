class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            index = ord(letter)
            if not node.letters[index]:
                node.letters[index] = WordNode()
            node = node.letters[index]
        node.end = True

    def search(self, word) -> bool:
        node = self.root
        def rec(idx, curr):
            if idx == len(word):
                if curr.end == True:
                    return True
                return False
            
            if word[idx] == ".":
                for nd in curr.letters:
                    if nd and rec(idx + 1, nd):
                        return True
                return False
            else:
                if curr.letters[ord(word[idx])] and rec(idx + 1, curr.letters[ord(word[idx])]):
                    return True
                return False
        return rec(0, node)
class WordNode:
    def __init__(self):
        self.letters = [None for _ in range(200)]
        self.end = False 
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)