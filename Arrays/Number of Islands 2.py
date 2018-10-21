class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """

        class DUS:
            def __init__(self):
                self.rank = {}
                self.parent = {}
                self.count = 0

            def find(self, x):
                if self.parent[x] != x:
                    return self.find(self.parent[x])
                return x

            def union(self, x, y):
                x, y = self.find(x), self.find(y)
                if x != y:
                    if self.rank[x] < self.rank[y]:
                        x, y = y, x
                    self.parent[y] = x
                    self.rank[x] += self.rank[x] == self.rank[y]
                    self.count -= 1

            def add(self, pos):
                pos = tuple(pos)
                i, j = pos
                self.parent[pos] = pos
                self.rank[pos] = 0
                self.count += 1
                for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nbr = (i + r, j + c)
                    if nbr in self.parent:
                        self.union(pos, nbr)
                return self.count

        res = []
        dus = DUS()
        for pos in positions:
            res.append(dus.add(pos))
        return res


m = 3
n = 3
positions = [[0,0], [0,1], [1,2], [2,1]]
print(Solution().numIslands2(m,n,positions))