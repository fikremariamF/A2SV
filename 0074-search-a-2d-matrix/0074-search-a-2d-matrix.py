class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for val in matrix:
            for num in val:
                if num == target:
                    return True
        return False