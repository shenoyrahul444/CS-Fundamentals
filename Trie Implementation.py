# Trie | (Insert and Search)
# Trie is an efficient information reTrieval data structure.
# Using Trie, search complexities can be brought to optimal limit (key length).
# If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree.
# Using Trie, we can search the key in O(M) time.
# However the penalty is on Trie storage requirements.
#
# Every node of Trie consists of multiple branches. Each branch represents a possible character of keys. We need to mark the last node of every key as end of word node.
# A Trie node field isEndOfWord is used to distinguish the node as end of word node.
# A simple structure to represent nodes of English alphabet can be as following,

# Version 1 - Trie for storing letters (
class Trie1:
    def __init__(self):
        self.root = {}

    def insert(self,word):
        curr = self.root

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]

        curr["*"] = "*"

    def search(self,word):
        curr = self.root

        for c in word:
            if c not in curr:
                return False
            curr = curr[c]

        return "*" in curr

    def startsWith(self,prefix):
        curr = self.root

        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]

        return True
    def getAllWithPrefix(self,prefix):
        curr = self.root

        for c in prefix:
            if c not in curr:
                return False

            curr = curr[c]
        # Now that we have reached a level where we have to go deep for all words henceforth, we explore(sort of like DFS)
        words = []
        self.explore(prefix,curr,words)
        return words

    def explore(self,prefix,curr,words):

        if "*" in curr:
            words.append(prefix)

        for letter, level in curr.items():
            if letter != "*":
                self.explore(prefix+letter,level,words)


sol = Trie1()
sol.insert("Rahul")
sol.insert("Goa")
sol.insert("Go")
sol.insert("Gone")
sol.insert("Going")
print(sol.startsWith("Gou"))
print(sol.getAllWithPrefix("Go"))



# Version 2 - Object Trie (Containing Nodes)
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEnd = False  # whether this node is an end of a word
        self.children = dict()  # map a char to the child node


class Trie2(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        currNode = self.root

        for c in word:
            if c not in currNode.children:
                currNode.children[c] = TrieNode()

            currNode = currNode.children[c]

        currNode.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currNode = self.root

        for c in word:
            if c not in currNode.children:
                return False

            currNode = currNode.children[c]

        return currNode.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currNode = self.root

        for c in prefix:
            if c not in currNode.children:
                return False

            currNode = currNode.children[c]

        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie2()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)