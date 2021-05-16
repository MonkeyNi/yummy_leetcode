class Solution:
    def memLeak(self, memory1: int, memory2: int):
        m1, m2 = memory1, memory2
        start = 1
        res = []
        while start <= max(m1, m2):
            # start from the first stidck
            if m2 > m1:
                m2 -= start
            else:
                m1 -= start
            start += 1
        return [start, m1, m2]