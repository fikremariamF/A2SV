class Solution:
    def hIndex(self, citations: List[int]) -> int:
        current = 0
        maxHidx = 0
        while current < len(citations):
            if len(citations) - current <= citations[current]:
                maxHidx = max(len(citations) - current, maxHidx)
            current += 1
        return maxHidx