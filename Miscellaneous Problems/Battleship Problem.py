
# BEST SOLUTION - 1 (45 milliseconds)
class Solution1(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board) == 0: return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    count += 1
        return count

# SOLUTION - 2 USING DFS (60 milliseconds)

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if board == None or board == []:
            return 0
        h = len(board)
        w = len(board[0])
        visited = [False] * (h * w)
        battleship_count = 0
        for row in range(h):
            for col in range(w):
                if board[row][col] == "X" and visited[row * w + col] == False:
                    if self.explore(row, col, w, h, board, visited):
                        battleship_count += 1
        return battleship_count

    def explore(self, row, col, w, h, board, visited):
        visited[row * w + col] = True
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for r, c in neighbors:
            if 0 <= row + r < h and 0 <= col + c < w:
                if board[row + r][col + c] == "X" and visited[(row + r) * w + (c + col)] == False:
                    self.explore(row + r, col + c, w, h, board, visited)
        return True
