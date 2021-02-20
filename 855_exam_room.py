import bisect


class ExamRoom:
    """
    Use suitable data strucure to solve the problem
    More ideal situation: 
        Save ordered length directly (instead of compute it every time)
            * need extrac space to save start and end
    """

    def __init__(self, N: int):
        self.N = N
        self.seat_ind = []

    def seat(self):
        N = self.N
        seat_ind = self.seat_ind
        if not seat_ind:
            res = 0
        else:
            d, res = seat_ind[0], 0
            # compute largest distance
            for a, b in zip(seat_ind, seat_ind[1:]):
                if (b-a)//2 > d:
                    d, res = (b-a)//2, (b+a)//2
            # get the last
            if N - 1 > seat_ind[-1] + d:
                res = N - 1
        # O(logN) save ordered length
        bisect.insort(seat_ind, res)
        return res
        
    def leave(self, p: int):
        self.seat_ind.remove(p)
        

test = ExamRoom(10)
print(test.seat())
print(test.seat())
print(test.seat())
print(test.seat())
print(test.leave(4))
print(test.seat())




# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)