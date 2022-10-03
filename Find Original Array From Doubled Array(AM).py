class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        length = len(changed)
        first, second = 0 ,0
        while True:
            if changed[first] * 2 == changed[second] and first != second:
                changed.pop(second)
                first += 1
            elif changed[first] * 2 < changed[second]:
                return []
                break
            elif changed[first] * 2 >= changed[second]:
                second += 1
            
            if second == len(changed):
                break
        if len(changed) == length/2:
            return changed
        return []
        
