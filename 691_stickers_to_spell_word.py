from collections import Counter


class Solution:
    def minStickers(self, stickers, target):
        s_dic = [Counter(s) for s in stickers]
        d_dic = Counter(target)
        print(f'S: {s_dic}')
        print(f'D: {d_dic}')
        # [1].shape
        ans = 0
        # left = len(d_dic)
        while len(d_dic):
            best = []
            match_num = 0
            for stick in s_dic:
                min_m, matched_s = self.match(stick, d_dic)
                matched = len(matched_s) 
                if matched > match_num:
                    match_num = matched
                    best = matched_s
            print(f'Res : {min_m, matched_s}')
            if match_num:
                for d in best:
                    d_dic[d] = d_dic[d] - min_m
                    if not d_dic[d]:
                        del d_dic[d]
                ans += min_m
            # import pdb; pdb.set_trace()
            print(f'Res: {d_dic}')
        return ans
    
    def match(self, stick, target):
        min_m = float('inf')  # current maxnimum matched
        matched_s = []
        for t in target:
            if stick[t]:
                min_m = min(min_m, target[t])
                # ans += 1
                matched_s.append(t)
        print(f'Match : {min_m, matched_s}')
        return min_m, matched_s
        

test = Solution()

stickers = ["with","example","science"]
target = "thehat"
print(test.minStickers(stickers, target))