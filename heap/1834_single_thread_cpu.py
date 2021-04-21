import heapq


class Solution:
    """
    CPU will process all tasks (which can be processed) with shortest processing time
    """
    def getOrder(self, tasks):
        """
        Heap problem, O(nlogn)
        Args:
            tasks ([list]): [[start_time, process_time]]
        """
        res = []
        sort_t = sorted([[t[0], t[1], i] for i, t in enumerate(tasks)]) # sort by start time and record the original ind
        start_time = sort_t[0][0]
        i = 0
        h = []
        while len(res) < len(tasks):
            # push tasks that can be processed to heap
            while i < len(tasks) and sort_t[i][0] <= start_time:
                heapq.heappush(h, (sort_t[i][1], sort_t[i][2]))
                i += 1
            # if there are tasks in heap, just pop it
            if h:
                pro, ind = heapq.heappop(h)
                start_time += pro
                res.append(ind)
            # cpu is idle, just skip to the next task
            else:
                if i < len(tasks):
                    start_time = sort_t[i][0]
        return res


test = Solution()
tasks = [[1,2],[2,4],[3,2],[4,1]]
res = test.getOrder(tasks)
print(res)


