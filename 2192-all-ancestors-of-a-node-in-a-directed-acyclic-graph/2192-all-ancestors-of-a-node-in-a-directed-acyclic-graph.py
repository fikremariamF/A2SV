class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # ancestors = [set() for _ in range(n)]
        
        indegrees = [0 for _ in range(n)]
        graph = defaultdict(set)
        ends = set()
        for frm, to in edges:
            graph[frm].add(to)
            indegrees[to] += 1
        
        output = [set() for _ in range(n)]
        queue = deque()
        
        for idx in range(n):
            if indegrees[idx] == 0:
                queue.append(idx)
        
        while queue:
            popped = queue.popleft()
            
            for node in graph[popped]:
                output[node].add(popped)
                output[node] = output[node].union(output[popped])
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)
                
        for idx in range(len(output)):
            output[idx]  = sorted(output[idx])
            
        
        return output