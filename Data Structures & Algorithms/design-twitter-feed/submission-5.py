class Twitter:

    def __init__(self):
        self.time = 0
        self.userToTweet = defaultdict(list)
        self.userToFollow = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.userToTweet[userId].append((self.time, tweetId))
        self.userToFollow[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        heap = []

        for user in self.userToFollow[userId]:
            time, tweetId = self.userToTweet[user][-1]
            heapq.heappush(heap, (-time, tweetId, user, -1))
        while heap and len(tweets) < 10:
            _, tweetId, userId, idx = heapq.heappop(heap)
            tweets.append(tweetId)
            idx -= 1
            if abs(idx) <= len(self.userToTweet[userId]):
                time, tweetId = self.userToTweet[userId][idx]
                heapq.heappush(heap, (-time, tweetId, userId, idx))
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userToFollow[followerId]:
            self.userToFollow[followerId].remove(followeeId)

        
