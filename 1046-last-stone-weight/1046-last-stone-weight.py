class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: x * -1, stones))
        heapify(stones)
        while len(stones) > 1:
            stone1 = heappop(stones)
            stone2 = heappop(stones)
            heappush(stones, -1 * abs(stone1 + (- stone2)))
        return abs(stones[0])