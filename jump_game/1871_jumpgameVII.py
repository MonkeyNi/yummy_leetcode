import collections
from collections import deque

class Solution:
    """
    BSF problem;
    Use deque, for each iteration, we need to add qualified ind to queue;
    To avoid duplicate 'checking', we use 'max_reach' to record the max ind that last iter can reach;
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def canReach(self, s, minJump, maxJump):
        if int(s[-1]):
            return False

        q = deque([0])
        max_reach = 0
        while q:
            cur_ind = q.popleft()
            for j in range(max(cur_ind+minJump, max_reach), min(cur_ind+maxJump+1, len(s))):
                if s[j] == '0':
                    if j == len(s)-1:
                        return True
                    q.append(j)
            max_reach = cur_ind + maxJump
        return False

test = Solution()
s = "011010"
minJ = 2
maxJ = 3
res = test.canReach(s, minJ, maxJ)
print(res)