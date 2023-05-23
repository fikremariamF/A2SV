class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
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
        
        equalOperations = []
        unEqualOperations = []
        
        for equation in equations:
            if equation[1] == "=":
                equalOperations.append(equation)
            else:
                unEqualOperations.append(equation)
        
        for equation in equalOperations:
            union(equation[0], equation[3])
        
        for equation in unEqualOperations:
            if connected(equation[0], equation[3]) and equation[1] == "!":
                return False
        return True