class Solution:
    def in_bound(self, i, j, grid):
        return 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0])

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        
        def bfs(i, j, grid):
            if not self.in_bound(i, j, grid) or grid[i][j] == -1:
                return 
            visited = [[False] * len(grid[0]) for _ in range(len(grid))]
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q = deque()
            q.append((i, j, 0))
            while q:
                r, c, dist = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not self.in_bound(nr,nc, grid) or grid[nr][nc] == -1:
                        continue
                    if grid[nr][nc] == 0:
                        grid[i][j] = dist + 1
                        return
                    if not visited[nr][nc]:
                        q.append((nr,nc,dist + 1))
                        visited[nr][nc] = True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1 and grid[i][j] != 0:
                    bfs(i,j,grid)


