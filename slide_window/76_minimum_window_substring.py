import collections
# import pysnooper

class Solution:
    
    # @pysnooper.snoop()
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        missing, target = len(t), collections.Counter(t)
        i = start = end = 0
        
        for j, char in enumerate(s, 1):  # remember, start from 1!!!
            # move left pointer, find the statisfied interval
            missing -= target[char] > 0
            target[char] -= 1
            
            # move right pointer, find the best interval
            if not missing:
                while i < j and target[s[i]] < 0:  # negative means that there are duplicates
                    target[s[i]] += 1
                    i += 1

                if not end or j-i <= end-start:
                    start, end = i, j
        return s[start:end]
    
    def minWindow_2(self, s: str, t: str):
        if not s or not t:
            return ""
        needs = collections.Counter(t)
        missing = len(t)
        st = e = j = 0
        for i, c in enumerate(s, start=1):
            missing -= needs[c] > 0
            needs[c] -= 1

            if not missing:
                while j < i and needs[s[j]] < 0:
                    needs[s[j]] += 1
                    j += 1
                
                if not e or i-j < e-st:
                    st, e = j, i
        return s[st:e]


if __name__ == "__main__":
    test = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(test.minWindow_2(s, t))