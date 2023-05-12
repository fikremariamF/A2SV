from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		self.adj = adj
		self.visited = set()
        for idx in range(v):
            if idx not in self.visited:
                if self.dfs(idx, set(), None) == False:
                    return 1
        return 0
    def dfs(self, idx, currPath, prev = None):
        currPath.add(idx)
        for node in self.adj[idx]:
            if prev == None or node != prev:
                if node in currPath:
                    return False
                else:
                    if not self.dfs(node, currPath, idx):
                        return False
        self.visited.add(idx)
        currPath.remove(idx)
        return True

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends