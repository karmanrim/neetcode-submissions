class Solution:
    def in_bound(self, i, j, grid):
        return 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0])
    
    def bfs(self, i, j, grid):
        if not self.in_bound(i, j, grid) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0 
        area = 1
        q = deque()
        q.append((i, j))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not self.in_bound(nr, nc, grid) or grid[nr][nc] == 0:
                    continue
                area += 1
                grid[nr][nc] = 0
                q.append((nr, nc))
        return area
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.bfs(i, j, grid))

        return max_area