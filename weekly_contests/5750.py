from bisect import bisect_left as bl
class Solution:
    def maximumPopulation(self, logs):
        if not logs:
            return False
        # merge all, add population information (1, -1)
        bd = []
        for b, d in logs:
            bd.append([b, 1])
            bd.append([d-0.5, -1])
        # sort all
        bd = sorted(bd)
        res = 0
        mr = 0
        year = 0
        for b, n in bd:
            res += n
            if res > mr:
                mr = res
                year = b
        return year    


test = Solution()
logs = [[1993,1999],[2000,2010]]
logs = [[1950,1961],[1960,1971],[1970,1981]]
logs = [[1982,1998],[2013,2042],[2010,2035],[2022,2050],[2047,2048]]
logs = [[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]
logs = [[2008,2026],[2004,2008],[2034,2035],[1999,2050],[2049,2050],[2011,2035],[1966,2033],[2044,2049]]
res = test.maximumPopulation(logs)
print(res)