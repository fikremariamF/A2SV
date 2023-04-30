class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        visited = set()
        
        if "0000" in deadends or target in deadends:
            return -1
        
        locks = deque ([["0000", 0]])
        
        visited.add("0000")
        
        while locks and locks[0]:
            popped = locks.popleft()
            # print("popped", popped)
            curr = popped[0]
            dist = popped[1]
            # print("curr",curr)
            if curr == target:
                return dist
            lockCombinations = []
            # print(curr)
            for idx in range(4):
                temp = curr
                # print(temp)
                temp = list(temp)
                # print(idx, temp)
                num = int(temp[idx])
                num += 1
                if num > 9:
                    num = 0
                
                
                temp[idx] = str(num)
                
                lockCombinations.append("".join(temp))
                
                temp = curr + ""
                
                temp = list(temp)
                
                num = int(temp[idx])
                
                num -= 1
                
                if num < 0:
                    num = 9
                
                temp[idx] = str(num)
                lockCombinations.append("".join(temp))
                
            for comb in lockCombinations:
                if comb not in visited and comb not in deadends:
                    locks.append([comb,dist + 1])
                    visited.add(comb)
        return -1