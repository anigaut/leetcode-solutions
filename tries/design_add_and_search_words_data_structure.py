'''
- Whenever a wildcard is encountered, need to check for all possible paths from the wildcard's parent node that match what comes after the wildcard
- Use recursive DFS for this.
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            cur = node
            for j in range(i, len(word)):
                char = word[j]
                if char == ".":
                    for child in cur.children.values():
                        if dfs(child, j + 1):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            
            return cur.end_of_word
        
        return dfs(self.root, 0)
        




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)