class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        length = [1 for i in range(len(edges) + 1)]
        
        
        def representative(member):
            while member != parent[member]:
                member = parent[member]
            return member
		
        def union(member1, member2):
            root1 = representative(member1)
            root2 = representative(member2)

            if root1 != root2:
                if length[root1]  > length[root2]:
                    length[root1] += length[root2]
                    parent[root2]= root1
                else:
                    length[root2] += length[root1]
                    parent[root1]= root2
                    
        def connected(x, y):
            return representative(x) == representative(y)
        
        output = []
        for x,y in edges:
            if not connected(x,y):
                union(x,y)
            else:
                output = [x,y]
        return output
                