class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set([tuple(queen) for queen in queens])
        answer = []
        def is_bound(row, col):
            return 0 <= row < 8 and 0 <= col < 8
        
        def fun(row, col):
            new_x = king[0]
            new_y = king[1]
            while is_bound(new_x, new_y):
                new_x += row
                new_y += col
                if (new_x, new_y) in queens:
                    answer.append([new_x, new_y])
                    break
        DIR = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]  
        for row, col in DIR:
            fun(row, col)
            
        return answer
    