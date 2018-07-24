class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == []:
            return 0
        l, b = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < l and 0 <= j < b:
                if grid[i][j] == 1:
                    grid[i][j] = -1     # mark visited locations with -1 to not confuse with 0
                    return dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
                elif grid[i][j] == -1:
                    return 0

            return 1   # Add 1 when out of Bounds or grid[i][j] == 0

        maxPerimeter = 0
        for i in range(l):
            for j in range(b):
                if grid[i][j] == 1:
                    maxPerimeter = max(maxPerimeter, dfs(i, j))
        return maxPerimeter

sol = Solution()
mat = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
print(sol.islandPerimeter(mat))

