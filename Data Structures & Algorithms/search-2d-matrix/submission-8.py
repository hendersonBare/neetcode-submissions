class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lrow, rrow = 0, len(matrix)-1
        while (lrow<rrow):
            mid_row = rrow+lrow // 2
            if matrix[mid_row][0] == target:
                return True
            elif matrix[mid_row][0] > target:
                rrow = mid_row-1
            else: #matrix[mid_row+1][0] < target:
                lrow = mid_row
        mid_row = lrow
        l,r = 0, len(matrix[mid_row])-1
        while (l<=r):
            mid = r+l // 2
            if matrix[mid_row][mid] == target:
                return True
            elif matrix[mid_row][mid] > target:
                r = mid-1
            else:
                l = mid+1
        return False