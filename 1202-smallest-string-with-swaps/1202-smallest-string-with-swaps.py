class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
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
                    
        def connected(x, y):
            return representative(x) == representative(y)
        
        for num1, num2 in pairs:
            union(num1, num2)
        
        groups = defaultdict(list)
        for idx in range(len(s)):
            heappush(groups[representative(idx)],s[idx])
        # print(groups)
        output = []
        for idx in range(len(s)):
            output.append(heappop(groups[representative(idx)]))
        
        return "".join(output)
            
        
        