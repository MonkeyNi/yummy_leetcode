class Solution:
    def longestBeautifulSubstring(self, word):
        if len(word) < 5:
            return 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        start = end = 0
        cur_beaty = vowels[0]
        res = 0
        while end < len(word):
            # set start
            if word[start] != vowels[0]:
                start += 1
                end = start + 1
            else:
                # meet the order requirement, keep moving right pointer (end)
                if word[end] >= cur_beaty:
                    cur_beaty = word[end]
                    end += 1
                else:
                    # word[start:end+1] is not beauty, update left pointer (right)
                    if cur_beaty == vowels[-1]:
                        res = max(res, end-start)
                    start = end
                    cur_beaty = vowels[0]
        if cur_beaty == vowels[-1]:
            res = max(res, end-start)
        return res


test = Solution()
word = "aeiaaioaaaaeiiiiouuuooaauuaeiu" # 13
# word = "aeeeiiiioooauuuaeiou" # 5
# word = "a" # 0
res = test.longestBeautifulSubstring(word)
print(res)



        