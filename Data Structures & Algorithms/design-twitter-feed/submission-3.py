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
        for user in self.userToFollow[userId]:
            tweets.extend(self.userToTweet[user])
        tweets.sort(reverse=True)
        return [el[1] for el in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userToFollow[followerId]:
            self.userToFollow[followerId].remove(followeeId)

        
