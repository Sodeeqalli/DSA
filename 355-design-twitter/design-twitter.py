class Twitter:

    def __init__(self):
        self.followList = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.time = 0


        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []

        self.follow(userId,userId)

        for user in self.followList[userId]:
            index = len(self.userTweets[user])-1
            if index >= 0:
                time, tweetId = self.userTweets[user][index]
                minHeap.append([time, tweetId, user, index-1])
        
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, user, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.userTweets[user][index]
                heapq.heappush(minHeap, [time, tweetId, user, index-1])
        
        return res


                


        

        
        


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)