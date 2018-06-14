class Solution:
    def countIslands(self,matrix):
        """
        Input: List[[ 1/0 ]]
        Output : Integer
        :return:
        """

        if matrix == None or len(matrix) == 0:
            return 0

        l = len(matrix)
        b = len(matrix[0])
        number_of_islands = 0
        dus = DUS(l*b)

        for i in range(l):
            for j in range(b):
                if matrix[i][j] == 0:
                    continue

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
                    if 0<= i+row < l and 0<= j+col < b:
                        if matrix[i+row][j+col] == 1:
                            dus.union(i*b+j,(i+row)*b + (j+col))

        c = [0]*(l*b)

        for i in range(l):
            for j in range(b):

                if matrix[i][j] == 1:
                    x = dus.find(i*b + j)
                    if c[x]==0:
                        number_of_islands += 1
                        c[x]+=1
                    else:
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
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return

        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        elif self.rank[yRoot] > self.rank[xRoot]:
            self.parent[xRoot] = yRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1

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




