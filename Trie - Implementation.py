# """ Implementing Basic Trie - For efficient word lookups"""

# TRIE - BEST SOLUTION  300ms Leetcode
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.end = "**"

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        level = self.trie
        for c in word:
            if c in level:
                level = level[c]
            else:
                level[c] = {}
                level = level[c]
        level[self.end] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        level = self.trie
        for c in word:
            if c in level:
                level = level[c]
            else:
                return False
        return self.end in level

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        level = self.trie
        for c in prefix:
            if c in level:
                level = level[c]
            else:
                return False
        return True


# trie = Trie()
# trie.insert("Rahul")
# trie.insert("Raul")
# trie.insert("Urvi")
# trie.insert("Raunak")
# print(trie.getAll())
# print(trie.search("Rahul"))
#
# print(trie.startsWith("Ra"))
# trie.insert("Urvi")


#
# """ 1> Making a Simple Trie structure in Python """
# def make_trie(words):
#
#     trie = {}
#
#     for word in words:
#         temp_dict = trie
#
#         for letter in word:
#
#             temp_dict = temp_dict.setdefault(letter,{})
#
#         temp_dict["*"] = "*"
#     return trie
#
# names = ["abcdefghijklmnopqrstuvwxyz"]
#
# print(make_trie(names))
#
#
# """ 2> Implementation 2 - LEET CODE"""
#
#
# class Trie(object):
#     def __init__(self):
#         self.root = {}
#
#     def insert(self, word):
#         cur = self.root
#         for x in word:
#             if x not in cur:
#                 cur[x] = {}
#             cur = cur[x]
#         cur['#'] = '#'
#
#     def search(self, word):
#         cur = self.root
#         for x in word:
#             if x not in cur:
#                 return False
#             cur = cur[x]
#         if '#' in cur:
#             return True
#         return False
#
#     def startsWith(self, prefix):
#         cur = self.root
#         for x in prefix:
#             if x not in cur:
#                 return False
#             cur = cur[x]
#         return True


