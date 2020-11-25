import collections
import pysnooper

# @pysnooper.snoop()
def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ''
    # set target needs
    need, missing = collections.Counter(t), len(t)
    i = start = end = 0
    for j, c in enumerate(s, 1):
        # update missing if c in t
        missing -= need[c] > 0
        # set unreleated char:value
        need[c] -= 1 ### IMPORTANT
        print(f'Outer: {need}')
        # if j (right end) move enough and s[i:j] inclue t, then update i (left)
        if not missing:
            while i<j and need[s[i]] < 0: ### IMPORTANT: only update start (i) when there is a new replicate target char
                # with pysnooper.snoop():
                print(f'Inner {need}, {s[i:j]}')
                need[s[i]] += 1 ### IMPORTANT
                i += 1
            if not end or j-i <= end-start: # to the end or get a smaller window
                start, end = i, j
    return s[start:end]

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t))