class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        vertices = defaultdict(int)
        edges = set()
        for road in roads:
            vertices[road[0]] += 1
            vertices[road[1]] += 1
            edges.add((road[0],road[1]))
            edges.add((road[1], road[0]))
        # print(vertices)
        output = 0
        for i in range(n):
            for j in range(i+1,n):
                network = vertices[i] + vertices[j]
                # print(network, i,j)
                if (i,j) in edges:
                    output = max(network - 1, output)
                else:
                    output = max(network, output)
        return output
            