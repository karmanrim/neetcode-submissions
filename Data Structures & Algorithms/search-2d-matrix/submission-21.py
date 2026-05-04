class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        r = n * m
        while r - l > 1:
            k = (r + l) // 2
            k_n = k // m
            k_m = k % m
            if matrix[k_n][k_m] <= target:
                l = k
            else:
                r = k
        return True if matrix[l // m][l % m] == target else False
