class Trie:
    def __init__(self):
        self.root = {}
        self.end = "*"

    def insert(self, word):
        level = self.root

        for c in word:
            if c not in level:
                level[c] = {}

            level = level[c]
        level[self.end] = self.end

    def getAllWithPrefix(self, prefix):
        level = self.root

        for c in prefix:
            if c not in level:
                return False
            level = level[c]
        res = []
        self.getAll(prefix, level, res)
        return res

    def getAll(self, prefix, level, res):

        if self.end in level:
            res.append(prefix)

        for c,l1 in level.items():
            if c != self.end:
                self.getAll(prefix + c, l1, res)


t = Trie()
t.insert("Rahul")
t.insert("Rekha")
t.insert("Rajesh")
# print(t)
print(t.getAllWithPrefix("R"))