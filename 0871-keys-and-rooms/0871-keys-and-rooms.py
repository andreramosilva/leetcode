class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        self.dfs(rooms,0,visited)
        return all(visited)
        
    def dfs(self,rooms,room,visited):
        visited[room] = True
        for key in rooms[room]:
            if not visited[key]:
                self.dfs(rooms,key,visited)
