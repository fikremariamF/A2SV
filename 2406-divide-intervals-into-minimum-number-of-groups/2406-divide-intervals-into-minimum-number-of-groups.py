class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        dict = collections.Counter()
        
        for s,e in intervals:
            dict[s] += 1
            dict[e+1] -= 1
        best= 0
        current = 0
        
        for k in sorted(dict.keys()):
            current += dict[k]
            best = max(best, current)
        return best
        
            
            
            
            