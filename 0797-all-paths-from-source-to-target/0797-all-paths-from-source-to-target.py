class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = set()
        path = []
        def travers(node):
            path.append(node)
            if node == len(graph) - 1:
                # print(path)
                paths.add(tuple(path))
                path.pop()
                return 
            for nd in graph[node]:
                travers(nd)
            path.pop()
            return
        travers(0)
        # print(paths)
        return paths
            
            