class Solution:
    """
    The key idea is that:
        1. every number should has only one position after sorted-concate;
        2. so if M is the pre_n max, and M is located at the right position (in this question, it equals to index),
            It means that we can split at this position.
    """
    def maxChunksToSorted(self, arr):
        pre_max = ans = 0
        for i, a in enumerate(arr):
            pre_max = max(pre_max, a)
            ans += (pre_max == i)
        return ans