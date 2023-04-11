class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ending = set()
        output = []
        for edge in edges:
            ending.add(edge[1])
        for num in range(0, n):
            if num not in ending:
                output.append(num)
        return output