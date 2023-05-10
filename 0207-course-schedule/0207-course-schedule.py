class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        inDegrees = [0 for _ in range(numCourses)]
        
        graph = defaultdict(set)
        for course, prerequisite in prerequisites:
            graph[prerequisite].add(course)
            inDegrees[course] += 1
        
        # visited = set()
        
        queue = deque()
        for idx in range(numCourses):
            if inDegrees[idx] == 0:
                queue.append(idx)
        
        while queue:
            idx = queue.popleft()
            
            for course in graph[idx]:
                inDegrees[course] -= 1
                if inDegrees[course] == 0:
                    queue.append(course)
        
        if sum(inDegrees) == 0:
            return True
        return False
        