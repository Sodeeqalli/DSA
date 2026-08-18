class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #this looks like a dependency graph to me
        n = len(rooms)
        visited = [False]*n
        keys = []
        visitCount = 0
        for key in rooms[0]:
            keys.append(key)
        visited[0] = True
        visitCount = 1
        print(keys)

        while keys:
            curKey = keys.pop()
            if visited[curKey] == True:
                continue
            print(curKey)
            visited[curKey] = True
            visitCount += 1
            print(visited, visitCount)
            if visitCount == n:
                return True
            
            for k in rooms[curKey]:
                if visited[k] == True:
                    continue
                keys.append(k)
            
        return visitCount == n


        