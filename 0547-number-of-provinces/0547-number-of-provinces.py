class Solution:
    def dfs(self, node,isConnected):  
        self.visited.add(node)
        for neighbour in range(len(isConnected[node])):#(O(N))
            if neighbour not in self.visited and isConnected[node][neighbour]==1:
                self.dfs(neighbour,isConnected)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        counter = 0
        for i in range(len(isConnected)):
            if i not in self.visited:
                self.dfs(i,isConnected)
                counter+=1
        return counter
                