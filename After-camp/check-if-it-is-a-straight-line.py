class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def calculateSlope(cord1, cord2):
            top = (cord2[0]-cord1[0])
            bottom = (cord2[1]-cord1[1])
            if not bottom:
                return float("inf")
            return top/bottom
        
        if len(coordinates) == 2:
            return True
        slope = calculateSlope(coordinates[0], coordinates[1])
        for i  in range(2,len(coordinates)):
            if calculateSlope(coordinates[i-1], coordinates[i]) != slope:
                return False
        return True
                
            
        