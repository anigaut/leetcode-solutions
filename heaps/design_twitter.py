import heapq
from typing import Any, List

class Twitter:

    def __init__(self):
        self.users: dict[int, dict[str, Any]] = {}
        self.time = 0

    def add_user(self, userId):
        details = {}
        details["tweets"] = []
        details["following"] = set()
        details["followers"] = set()

        self.users[userId] = details

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.users:
            self.add_user(userId)
        
        self.time -= 1
        user = self.users[userId]
        user["tweets"].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        if not userId in self.users:
            self.add_user(userId)
        
        user = self.users[userId]
        tweet_heap = []
        tweet_heap += user["tweets"][-10:]

        for follow in user["following"]:
            tweet_heap += self.users[follow]["tweets"][-10:]
        
        heapq.heapify(tweet_heap)

        while tweet_heap and len(feed) < 10:
            feed.append(heapq.heappop(tweet_heap)[1])
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.users:
            self.add_user(followerId)
        if not followeeId in self.users:
            self.add_user(followeeId)

        if followerId != followeeId:
            follower = self.users[followerId]
            followee = self.users[followeeId]

            follower["following"].add(followeeId)
            followee["followers"].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.users:
            self.add_user(followerId)
        if not followeeId in self.users:
            self.add_user(followeeId)

        if followerId != followeeId:
            follower = self.users[followerId]
            followee = self.users[followeeId]

            if followeeId in follower["following"]:
                follower["following"].remove(followeeId)
                followee["followers"].remove(followerId)