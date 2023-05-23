class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]
        length = [1 for i in range(26)]
        
        
        def representative(member):
            # print(member, parent)
            while member != parent[member]:
                member = parent[member]
            # print(member, parent)
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
        
        for idx in range(len(s1)):
            # print(ord(s1[idx]) - 97, ord(s2[idx]) - (97))
            union(ord(s1[idx]) - 97, ord(s2[idx]) - 97)
        # print(parent)   
        groups = defaultdict(list)
        for idx in range(26):
            # print(chr(idx + 97))
            
            groups[chr(representative(idx) + 97)].append(chr(idx + 97))
            
        output = []
        # print(groups)
        for letter in baseStr:
            # print("AHOY", ord(letter) - 97)
            temp_parent = chr(representative(ord(letter) - 97) + 97)
            letters = groups[temp_parent]
            letters.sort()
            output.append(letters[0])
        
        # print(groups)
        return "".join(output)