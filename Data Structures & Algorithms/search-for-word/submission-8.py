class Solution:
    def in_bound(self, i, j, board):
        return (i >= 0 and i < len(board)) and (j >= 0 and j < len(board[0]))
    
    def bfs(self, i, j, board, word, k, visited):
        if not self.in_bound(i, j, board) or word[k] != board[i][j]:
            return False 
        if k == len(word) - 1 and word[k] == board[i][j]:
            return True
        visited[i][j] = True
        next_steps = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
        for new_i, new_j in next_steps:
            if self.in_bound(new_i, new_j, board) and not visited[new_i][new_j]:
                flag = self.bfs(new_i, new_j, board, word, k + 1, visited)
                if flag:
                    return True
        visited[i][j] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        def find_first_letter(board, word):
            res = []
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        res.append([i,j])
            return res
        
        start_points = find_first_letter(board, word)
        print(start_points)
        if len(start_points) == 0:
            return False
        for start_point in start_points:
            visited = [[False for _ in range(len(el))] for el in board]
            flag = self.bfs(start_point[0], start_point[1], board, word, 0, visited)
            if flag:
                return True
        return False

                        