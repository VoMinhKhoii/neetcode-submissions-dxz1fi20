class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Treat this 2D like a 1D
        m,n = len(matrix), len(matrix[0])
        left, right = 0, (m * n) - 1

        while left <= right:
            mid = int((left + right) / 2)
            
            row = int(mid / n)
            col = mid % n

            if target == matrix[row][col]:
                return True
            if target >= matrix[row][col]:
                left = mid + 1
            else: 
                right = mid - 1
        return False

        