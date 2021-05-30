import heapq as hp
class Solution:
    """
    Key points:
    1. for task jth, it can at or after jth second;
    2. if there are multiple runnable tasks and multiple available servers, then those 
        tasks can be started at the same time;
    """
    def assignTasks(self, servers, tasks):
        # Two headpq
        # first one save all available servers
        # poping by weight and index
        # second one save all using servers
        # poping by time
        ava_servers = [[weight, ind, 0] for ind, weight in enumerate(servers)]
        inUsing_servers = []
        hp.heapify(ava_servers)
        res = []
        for t, task in enumerate(tasks):
            # find all ava servers from inUsing and put them to ava_servers
            while inUsing_servers and inUsing_servers[0][0] <= t or not ava_servers:
                time, weight, ind = hp.heappop(inUsing_servers)
                hp.heappush(ava_servers, [weight, ind, time])
            # find current ava server
            weight, ind, time = hp.heappop(ava_servers)
            res.append(ind)
            hp.heappush(inUsing_servers, [max(time, t)+task, weight, ind])
        return res

test = Solution()
servers = [3,3,2]
tasks = [1,2,3,2,1,2]
# servers = [5,1,4,3,2]
# tasks = [2,1,2,4,5,2,1]
# servers = [10,63,95,16,85,57,83,95,6,29,71]
# tasks = [70,31,83,15,32,67,98,65,56,48,38,90,5]
res = test.assignTasks(servers, tasks)
print(res)
