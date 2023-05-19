class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        tracker = {}
        for road in roads:
            tracker[(road[0], road[1])] = road
        
        parent = [i for i in range(n + 1)]
        length = [1 for i in range(n + 1)]
        
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
        
        for city1, city2, distance in roads:
            union(city1, city2)
        
        minimum = float("inf")
        # print(parent)
        for x,y,z in roads:
            parent0 = representative(1)
            parentX = representative(x)
            parentY = representative(y)
            if parent0 == parentX:
                minimum = min(z, minimum)
        return minimum
                    
        