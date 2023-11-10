class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # Perform BFS to find the path and calculate the answer for each query
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited = set()
            queue = deque([(start, 1.0)])
            while queue:
                current, current_product = queue.popleft()
                if current == end:
                    return current_product
                visited.add(current)
                for neighbor, value in graph[current].items():
                    if neighbor not in visited:
                        queue.append((neighbor, current_product * value))
            return -1.0

        # Calculate answers for each query
        results = [bfs(start, end) for start, end in queries]
        return results