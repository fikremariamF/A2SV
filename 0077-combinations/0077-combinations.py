class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        arr = []
        def generateComp(maxVal = 0):
            if arr and len(arr) == k:
                output.append(arr[:])
                return 
            
            for val in range(maxVal + 1, n + 1):
                arr.append(val)
                generateComp(val)
                arr.pop()
                
            return
        
        generateComp()
        
        return output