class Solution:
    def countIslands(self,matrix):
        """
        Input: List[[ 1/0 ]]
        Output : Integer
        :return:
        """

        if matrix == None or len(matrix) == 0:
            return 0

        l,b = len(matrix),len(matrix[0])
        number_of_islands = 0
        dus = DUS(l*b)

        for i in range(l):
            for j in range(b):
                if matrix[i][j] == 1:
                    neighbors = [
                        (-1,-1),
                        (-1,0),
                        (-1,1),
                        (0,-1),
                        (0,1),
                        (1,-1),
                        (1,0),
                        (1,1)
                    ]

                    for row,col in neighbors:
                        if 0<= i+row < l and 0<= j+col < b and  matrix[i+row][j+col] == 1:
                                dus.union(i*b+j,(i+row)*b + (j+col))

        c = [0]*(l*b)

        for i in range(l):
            for j in range(b):
                if matrix[i][j] == 1:
                    x = dus.find(i*b + j)
                    if c[x]==0:
                        number_of_islands += 1
                    c[x]+=1
        return number_of_islands

class DUS:  # Disjoint Union Set
    def __init__(self,n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0]*n

    def find(self,x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return x


    def union(self,x,y):
        xRoot,yRoot = self.find(x),self.find(y)

        if xRoot == yRoot:
            return

        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        elif self.rank[yRoot] > self.rank[xRoot]:
            self.parent[xRoot] = yRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1

class DUS:
    def __init__(self):
        self.rank = {}
        self.parent = {}
        self.count = 0

    def find(self,pos):
        if self.parent[pos] != pos:
            return self.find(pos)
        return pos
    def union(self,x,y):
        x,y = self.find(x),self.find(y)
        if x == y:
            return 0
        if self.rank[x] < self.rank[y]:
            x,y=y,x
        self.parent[y] = x
        self.rank[x] =
    def add(self,pos):
        self.parent[pos] = pos


class Solution2:
    def numIslands2(self, m, n, positions):
        parent, rank, count = {}, {}, [0]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                if rank[x] < rank[y]:
                    x, y = y, x
                parent[y] = x
                rank[x] += rank[x] == rank[y]
                count[0] -= 1

        def add(pos):
            parent[post] = pos
            rank[x] = 0
            count[0] += 1
            neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
            for y in :
                if y in parent:
                    union(x, y)
            return count[0]

        return map(add, positions)
sol = Solution()
# matrix = [[1,0,0],[0,0,0],[0,1,0]]
matrix = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]
print(sol.countIslands(matrix))
