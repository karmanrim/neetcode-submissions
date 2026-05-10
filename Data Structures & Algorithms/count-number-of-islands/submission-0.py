class Solution:
    def in_bound(self, i, j, grid):
        return 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0])

    def bfs(self, i, j, grid):
        if not self.in_bound(i, j, grid) or grid[i][j] == "0":
            return 
        
        grid[i][j] = "0"
        next_steps = ((i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j))
        for new_i, new_j in next_steps:
            self.bfs(new_i, new_j, grid)
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