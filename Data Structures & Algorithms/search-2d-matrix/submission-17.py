class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        r = m * n - 1
        l = 0
        while l <= r:
            mid = l + (r - l) // 2
            mid_n = mid % n
            mid_m = mid // n
            print(mid_m, mid_n)
            if matrix[mid_m][mid_n] > target: 
                r = mid - 1
            elif matrix[mid_m][mid_n] < target: 
                l = mid + 1
            else:
                return True
        return False