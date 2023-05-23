class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = dict()
        length = dict()
        
        
        def representative(member):
            if member not in parent:
                parent[member] = member
                length[member] = 1
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
                    
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(tuple(stones[i]), tuple(stones[j]))
        
        groups= defaultdict(int)
        
        for stone in parent:
            groups[representative(stone)] += 1
        
        # print(groups)
        longest = 0
        for rep in groups:
            longest += groups[rep] - 1
        
        return longest
            
        
        