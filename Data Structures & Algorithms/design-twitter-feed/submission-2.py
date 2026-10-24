class Twitter:

    def __init__(self):
       self.userToTweets = defaultdict(list)
       self.userToFollow = defaultdict(set)
       self.timestamp = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.userToTweets[userId].append([self.timestamp, tweetId])
        self.userToFollow[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for idx in self.userToFollow[userId]:
            for tweet in self.userToTweets[idx]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)
        heap.sort(reverse=True)
        return [el[1] for el in heap] 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userToFollow[followerId]:
            self.userToFollow[followerId].remove(followeeId)
        
