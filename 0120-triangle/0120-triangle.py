class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            if row == 0:
                return triangle[0][0]
            
            val = 0
            if 0 < col < len(triangle[row]) - 1:
                val = min(dp(row-1, col), dp(row-1, col - 1))
            elif 0 == col:
                val = dp(row - 1, col)
            elif col == len(triangle[row]) - 1:
                val = dp(row - 1, col - 1)
            return triangle[row][col] + val
        minn = float("inf")
        for idx in range(len(triangle[-1])):
            minn = min(dp(len(triangle) - 1, idx), minn)
        return minn