class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = dict()
        for edge in edges:
            if edge[0] in counter:
                counter[edge[0]] += 1
            else:
                counter[edge[0]] = 1
            
            if edge[1] in counter:
                counter[edge[1]] += 1
            else:
                counter[edge[1]] = 1
                
        return max(counter, key = lambda x: counter[x])