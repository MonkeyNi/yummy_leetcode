from collections import Counter
from collections import defaultdict

def max_string(s, k):

    # sort string first
    s = sorted(s, reverse=True)
    max_n = len(s)

    s_d = Counter(s)
    s_k = list(s_d.keys())
    # record pre string
    s_n = defaultdict(int)
    pre_s = s[0]

    res = []
    for i in range(max_n):
        # append largest first
        for sk in s_k:
            if s_d[sk] > 0 and s_n[sk] < k:
                res.append(sk)
                s_n[sk] += 1
                s_d[sk] -= 1
                # updated or not
                pre_s = sk
                break
            # reset
            else:
                s_n[sk] = 0
    return ''.join(res)

# s = 'cccdf'
s = 'aaaaa'
k =2
# ss = ['', 'ab', 'aaaaa', 'cccdf', 'xzdfsdxxxzs']
# for s in ss:
#     for k in range(3):
#         # print(max_string(s, k))
#         print(f'{s, k}: {max_string(s, k)}')
print(max_string(s, k))


