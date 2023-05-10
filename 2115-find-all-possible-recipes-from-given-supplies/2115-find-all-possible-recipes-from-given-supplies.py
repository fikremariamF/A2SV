class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        inDegrees = defaultdict(int)
        
        graph = defaultdict(set)
        
        for idx in range(len(recipes)):
            for ingredient in ingredients[idx]:
                graph[ingredient].add(recipes[idx])
                inDegrees[recipes[idx]] += 1
                
        queue = deque(supplies)
        output = []
        while queue:
            temp = queue.popleft()
            
            for recepy in graph[temp]:
                inDegrees[recepy] -= 1
                if inDegrees[recepy] == 0:
                    queue.append(recepy)
                    output.append(recepy)
        
        return output
        
        