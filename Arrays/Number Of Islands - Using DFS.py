class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # Edge Case
        if grid == None or grid == [] or grid == [[], [], []] or grid == [[]]:
            return 0

        h = len(grid)
        w = len(grid[0])
        self.h = h
        self.w = w

        cluster_count = 0
        visited = [[False for i in range(w)] for j in range(h)]

        self.visited = visited
        self.grid = grid

        for i in range(h):
            for j in range(w):

                if visited[i][j] == False and grid[i][j] == "1":
                    self.DFS(i, j)
                    cluster_count += 1
        return cluster_count

    def DFS(self, row, col):

        neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.visited[row][col] = True

        for r, c in neighbors:
            if self.isSafe(row + r, col + c):
                self.DFS(row + r, col + c)

    def isSafe(self, row, col):

        if 0 <= row < self.h and 0 <= col < self.w:
            if self.visited[row][col] == False and self.grid[row][col] == "1":
                return True
        return False

sol = Solution()
matrix = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","1"]]
print(sol.numIslands(matrix))