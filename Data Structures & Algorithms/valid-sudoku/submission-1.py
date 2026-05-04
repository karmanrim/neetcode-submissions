class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        blocs = {i: set() for i in range(9)}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val in rows[i]:
                    return False
                if val in cols[j]:
                    return False
                block_idx = i // 3 * 3 + j // 3
                if val in blocs[block_idx]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                blocs[block_idx].add(val)
        return True

