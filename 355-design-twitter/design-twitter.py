class Twitter:

    def __init__(self):
        self.followList = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.time = 0


        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        newsFeed = []

        users = set(self.followList[userId])
        users.add(userId)

        for user in users:
            tweets = self.userTweets[user]
            for time, tweetId in tweets:
                heapq.heappush(maxHeap, (time, tweetId))

        while maxHeap and len(newsFeed) < 10:
            newsFeed.append(heapq.heappop(maxHeap)[1])

        return newsFeed

        
        


        

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