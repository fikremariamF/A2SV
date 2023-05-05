class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = list(map(lambda x: -1 * x, piles))
        heapify(piles)
        # print(piles)
        for _ in range(k):
            temp = heappop(piles)
            heappush(piles, floor(temp/2))
        # print(piles)
        return -1 * sum(piles)