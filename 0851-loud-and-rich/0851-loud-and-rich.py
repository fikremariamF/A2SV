class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        ans = [999999999] * n
        visit = set()
        for rich, poor in richer:
            graph[poor].append(rich)
        for i in range(n):
            if i not in graph:
                graph[i] = []
        # print(graph)
        realans = [-1] * n
        def dfs(i, start):
            nonlocal ans
            if i != start or i == start:
                if quiet[i] < ans[start]:
                    ans[start] = quiet[i]
                    realans[start] = i
            elif graph[i] == [] and i == start:
                realans[i] = i
            if i in visit:
                return
            visit.add(i)
            for nx in graph[i]:
                dfs(nx, start)
        
        for i in range(n):
            dfs(i, i)
            visit.clear()

        return realans