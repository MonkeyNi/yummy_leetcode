from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions):
        # name, time, amout, city
        # 1. amount > 1000
        # 2. occurs within 60 mins with same name different city

        flag = [False for i in range(len(transactions))]
        # set id for each tran
        ind_t = [[t, i] for i, t in enumerate(transactions)]
        # Situation 1
        res = []
        for i, tran in enumerate(transactions):
            if int(tran.split(',')[2]) > 1000:
                if not flag[i]:
                    res.append(tran)
                    flag[i] = True
        
        # Situation 2
        sit2 = defaultdict(list)
        for i, tran_ind in enumerate(ind_t):
            tran, ind = tran_ind
            name, info = tran.split(',')[0], tran.split(',')[1:]
            sit2[name].append(tran_ind)

        for name in sit2:
            # sort by time
            infos = sorted(sit2[name], key=lambda x:int(x[0].split(',')[1]))
            for i in range(len(infos)):
                cur_i, ii = infos[i]
                _, time1, _, city1 = cur_i.split(',')
                for j in range(i+1, len(infos)):
                    com_i, jj = infos[j]
                    _, time2, _, city2 = com_i.split(',')
                    if city1 != city2 and abs(int(time1)-int(time2)) <= 60:
                        if not flag[ii]:
                            res.append(cur_i)
                            flag[ii] = True
                        if not flag[jj]:
                            res.append(com_i)
                            flag[jj] = True
        return res


test = Solution()
transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# transactions = ["alice,20,1220,mtv","alice,20,1220,mtv"]
# transactions = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
# transactions = ["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]
res = test.invalidTransactions(transactions)
print(res)


