class Node:
    def __init__(self, val):
        """
        Initialize your data structure here."""

        self.data = val
        self.childern = dict()
        self.endhere = False

class Trie:
    def __init__(self):
        # self.root = None
        self.root = Node(None)
    
    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        parent = self.root
        for i, char in enumerate(word):
            if char not in parent.childern:
                parent.childern[char] = Node(char)
            parent = parent.childern[char]

            if i == len(word)-1:
                parent.endhere = True
    
    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        
        parent = self.root
        for char in word:
            if char not in parent.childern:
                return False
            parent = parent.childern[char]
        return parent.endhere

    
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        parent = self.root
        for char in prefix:
            if char not in parent.childern:
                return False
            parent = parent.childern[char]
        return True
    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)