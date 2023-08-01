class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for i in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        queue = [0]
        q = 1 
        
        par = [0]*n 
        
        vis = [0]*n 
        vis[0] = 1 

        while q > 0:
            s = queue[-1]

            flag = True
            for z in adj[s]:

                if not vis[z]:
                    par[z] = s
                    flag = False
                    vis[z] = 1 
                    q += 1 
                    queue.append(z)
                    
            if flag:
                for z in adj[s]:
                    if z == par[s]:
                        continue
                    if hasApple[z]:
                        hasApple[s] = True
                        
                queue.pop()
                q -= 1 

        sm = sum(hasApple)-1 

        return max(0, 2*sm)