class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value,timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        searchList = self.timeMap[key]
        l = 0
        r = len(searchList)-1
        res = ""
        while l<=r:
            m = l + ((r-l)//2)
            if searchList[m][1] == timestamp:
                return searchList[m][0]
            elif searchList[m][1] < timestamp:
                res = searchList[m][0]
                l = m+1
            else:
                r = m - 1
        
        return res

    
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)