class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # for idx in range(len(tickets)):
        #     tickets[idx] = (idx, tickets[idx])
        queue = deque(tickets)
        boughtAll = False
        counter = 0
        while not boughtAll:
            counter += 1
            k -= 1
            temp = queue.popleft() - 1
            if temp != 0:
                queue.append(temp)
            if k == -1:
                k = len(queue) - 1
                if temp == 0:
                    break
                
        return counter