class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a,b = 0, len(matrix)-1

        while a < b:
            mid = (a+b)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if mid<len(matrix)-1 and matrix[mid+1][0]>target:
                    break
                else:
                    a = mid+1
            else:
                b = mid-1
        
        row = (a+b)//2
        i,j = 0, len(matrix[0])-1
        while i<=j:
            mid = (i+j)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                i = mid+1
            else:
                j=mid-1
        return False
