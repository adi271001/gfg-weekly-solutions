from collections import deque

class Solution:
    def avoidFire(self, n, m, x, y, arr):
        fire = [[10**9] * m for _ in range(n)]
        dist = [[10**9] * m for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    q.append([i,j])
                    fire[i][j] = 0
                    
        if not q:
            return 1
        
        dx, dy = [1,0,-1,0], [0,1,0,-1]
        
        while q:
            xx, yy = q.popleft()
            for i in range(4):
                nx, ny = xx + dx[i], yy + dy[i]
                if 0 <= nx < n and 0 <= ny < m and fire[nx][ny] > 1 + fire[xx][yy]:
                    fire[nx][ny] = 1 + fire[xx][yy]
                    q.append([nx,ny])
                    
        dist[x][y] = 0
        q.append([x,y])
        
        while q:
            xx, yy = q.popleft()
            if fire[xx][yy] <= dist[xx][yy]:
                continue
            for i in range(4):
                nx, ny = xx + dx[i], yy + dy[i]
                if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] > 1 + dist[xx][yy] and fire[nx][ny] > 1 + dist[xx][yy]:
                    dist[nx][ny] = 1 + dist[xx][yy]
                    q.append([nx,ny])
                    
        return int(dist[n-1][m-1] != 1e9)
