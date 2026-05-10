class Solution:
    def in_bound(self, i, j, grid):
        return 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0])

    def bfs(self, i, j, grid):
        q = deque()
        
        grid[i][j] = "0"
        q.append((i, j))
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc
                if not self.in_bound(new_r, new_c, grid) or grid[new_r][new_c] == "0":
                    continue
                q.append((new_r, new_c))
                grid[new_r][new_c] = "0"
        return 

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.bfs(i, j, grid)
                    counter += 1
        return counter