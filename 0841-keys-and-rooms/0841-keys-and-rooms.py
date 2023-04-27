class Solution:
    def visitRooms(self, key):
        self.visited.add(key)
        for newKey in self.graph[key]:
            if newKey not in self.visited:
                self.visitRooms(newKey)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.graph = dict()
        self.visited = set()
        for idx in range(len(rooms)):
            self.graph[idx] = set(rooms[idx])
        
        self.visitRooms(0)
        if len(self.visited) < len(rooms):
            return False
        return True