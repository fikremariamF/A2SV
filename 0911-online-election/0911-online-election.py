class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.presum = []
        tracker = {}
        maxVoted = persons[0]
        for idx in range(len(persons)):
            if persons[idx] in tracker:
                tracker[persons[idx]] += 1
            else:
                tracker[persons[idx]] = 1
            if tracker[persons[idx]] >= tracker[maxVoted]:
                maxVoted = persons[idx]
            self.presum.append([times[idx], maxVoted])
            
        # print(self.presum)
        return
    def q(self, t: int) -> int:
        left, right = 0, len(self.presum) - 1
        
        while left <= right:
            mid = (left + right)//2
            if self.presum[mid][0] == t:
                return self.presum[mid][1]
            elif self.presum[mid][0] > t:
                right = mid -1
            elif self.presum[mid][0] < t:
                left = mid + 1 
        return self.presum[right][1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(perlefts, times)
# param_1 = obj.q(t)