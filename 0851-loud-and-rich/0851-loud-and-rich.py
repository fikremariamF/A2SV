class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        neighbours = defaultdict(list)
        for a,b in richer:
            neighbours[b].append(a)
        output = [idx for idx in range(len(quiet))]
        
        visited = set()
        def dfs(idx):
            visited.add(idx)
            for n in neighbours[idx]:
                if n not in visited:
                    output[n] = dfs(n)
                if quiet[output[n]] < quiet[output[idx]]:
                    output[idx] = output[n]
            return output[idx]
        for num in range(len(quiet)):
            if num not in visited:
                output[num] = dfs(num)
            
        return output