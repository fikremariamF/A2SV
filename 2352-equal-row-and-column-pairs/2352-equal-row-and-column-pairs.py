class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # appends each column to the columns list changing them to a tuple
        columns = []
        for col in range(len(grid)):
            cur_col = []
            for row in range(len(grid)):
                cur_col.append(grid[row][col])
            columns.append(tuple(cur_col))
        # print(columns)
        
        #appends each row to the rows list changing each row to a tuple for comparison
        rows = []
        for row in range(len(grid)):
            cur_row = []
            for col in range(len(grid)):
                cur_row.append(grid[row][col])
            rows.append(tuple(cur_row))
        # print(rows)
        
        #counte the number of similar pairs
        counter = 0
        for row in rows:
            for col in columns:
                if row == col:
                    counter += 1
        return counter