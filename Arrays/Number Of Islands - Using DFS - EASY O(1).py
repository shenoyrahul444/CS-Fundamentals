class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        """
        self.grid = grid
        l, b = len(grid), len(grid[0])
        self.l = l
        self.b = b
        island_count = 0
        for i in range(l):
            for j in range(b):
                if grid[i][j]:
                    self.dfs(i, j)
                    island_count += 1
        return island_count

    def dfs(self, i, j):
        if 0 <= i < self.l and 0 <= j < self.b and self.grid[i][j]:
            self.grid[i][j]= 0
            self.dfs(i + 1, j)
            self.dfs(i - 1, j)
            self.dfs(i, j + 1)
            self.dfs(i, j - 1)


sol = Solution()
matrix = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","1"]]
print(sol.numIslands(matrix))