class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        memo = {}

        def dp(i, j):
            if i == -1:
                return j + 1 # remember add 1, since index start from 0
            if j == -1:
                return i + 1
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i-1, j-1)
            else:
                memo[(i, j)] = min(
                    dp(i-1, j), # delete
                    dp(i-1, j-1), # replace
                    dp(i, j-1) # add
                ) + 1
            return memo[(i, j)]
        
        return dp(len(word1)-1, len(word2)-1)

test = Solution()
word1 = "horse"
word2 = "ros"
res = test.minDistance(word1, word2)
print(res)