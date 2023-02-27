class Solution:
    def saveCivilians(self, n, m, grid):
        # code here
        civilians = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 'C']
        if not civilians:
            return True
        for i, j in civilians:
            for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] == 'T':
                    return False
        for i, j in civilians:
            for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] == 'E':
                    grid[x][y] = 'S'
        return True
