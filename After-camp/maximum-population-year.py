class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        items = [0 for _ in range(2051)]
        for birth, death in logs:
            items[birth] += 1
            items[death] -= 1
        maxx = 0
        for idx in range(1940, 2051):
            items[idx] += items[idx - 1]
            maxx = max(maxx, items[idx])
        # print(items[1940: 2051])
        # print(maxx)
        for idx in range(1940, 2051):
            if items[idx] == maxx:
                return idx
        return 0
            
        