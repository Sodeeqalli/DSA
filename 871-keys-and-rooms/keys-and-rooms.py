class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visitCount = 0
        visited = [False] * len(rooms)

        def dfs(room):
            nonlocal visitCount
            if visited[room] == True:
                return
            visited[room] = True
            visitCount += 1

            for nextRoom in rooms[room]:
                if visited[nextRoom] == False:
                    dfs(nextRoom)
            return
            
        dfs(0)
        return visitCount == len(rooms)
            
        


        

        



        