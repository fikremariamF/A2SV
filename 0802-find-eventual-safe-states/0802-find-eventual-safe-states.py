class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0 for _ in range(len(graph))]
        
        output = []
        def dfs(idx):
            if colors[idx] == 2:
                return True
            
            if colors[idx] == 3:
                return False
            
            colors[idx] = 2
            for tempIdx in graph[idx]:
                if dfs(tempIdx):
                    return True
            
            colors[idx] = 3
            return False
        
        for idx in range(len(colors)):
            if not dfs(idx):
                output.append(idx)
        output.sort()   
        return output