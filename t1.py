from collections import Counter
from collections import defaultdict

def getLargestString(s, k):
    # Write your code here
    s = sorted(s, reversed=True)
    s_dic = Counter(s)
    s_keys = list(s_dic.keys())

    needs = defaultdict(int)
    res = []
    i = 0
    while i < len(s_keys):
        sk = s_keys[i]
        ele = s_dic[sk]
        if needs[ele] < k:
            res.append(ele)
            needs[ele] += 1
        else:
