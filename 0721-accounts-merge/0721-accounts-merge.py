class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = dict()
        for account in accounts:
            idx = len(account) - 1
            while idx > 0:
                emails[account[idx]] = account[0]
                idx -= 1
        parent = dict()
        length = dict()
        
        # print(emails)
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
            # print("CALLED")
            if root1 != root2:
                # print("in here")
                if length[root1]  > length[root2]:
                    length[root1] += length[root2]
                    parent[root2]= root1
                else:
                    length[root2] += length[root1]
                    parent[root1]= root2
                    
        def connected(x, y):
            return representative(x) == representative(y)
        
        for account in accounts:
            # print(account)
            for i in range(1, len(account)-1):
                # print(account,i)
                union(account[1], account[i+1])
        
        groups = defaultdict(list)
        
        for email in emails:
            groups[representative(email)].append(email)
            
        output = []
        for group in groups:
            groups[group].sort()
            temp = [emails[group]] + groups[group]
            output.append(temp)
        return output
                