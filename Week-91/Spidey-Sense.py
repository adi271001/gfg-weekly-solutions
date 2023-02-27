from queue import Queue
class Solution:
    def shortestDistanceFromTheBomb(self, grid, n, m):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = Queue()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'B':
                    q.put((i, j, 0))
                    grid[i][j] = 0  # Replace 'B' with 0
                elif grid[i][j] == 'W':
                    grid[i][j] = -1

        while not q.empty():
            i, j, dist = q.get()
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if ni < 0 or ni >= n or nj < 0 or nj >= m or grid[ni][nj] != 'O':
                    continue
                grid[ni][nj] = dist + 1
                q.put((ni, nj, dist + 1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'O':
                    grid[i][j] = -1
