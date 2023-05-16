class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        length = [1 for i in range(n)]
        
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
        
        for num1, num2 in edges:
            union(num1, num2)
        
        return connected(source, destination)