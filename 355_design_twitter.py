from collections import defaultdict, deque
from itertools import count, islice
import heapq
# from typing import List

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = count(step=-1)  # must be negative 1
        self.follwee = defaultdict(set)
        self.tweets = defaultdict(deque)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].appendleft((next(self.time), tweetId))
        

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        sorted_me = heapq.merge(*(self.tweets[u] for u in self.follwee[userId] | {userId}))
        return [t for _, t in islice(sorted_me, 10)]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follwee[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follwee[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)