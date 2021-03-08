class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        
    def push(self, x: int) -> None:
        q_min = self.getMin()
        if q_min == None or x < q_min:
            q_min = x
        self.q.append((x, q_min))

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        if len(self.q) == 0:
            return None
        return self.q[-1][0]

    def getMin(self) -> int:
        if len(self.q) == 0:
            return None
        return self.q[-1][1]
        


minStack = MinStack()
print(minStack.push(0))
print(minStack.push(1))
print(minStack.push(0))
print(minStack.getMin()) # return -3
print(minStack.pop())
# print(minStack.top())   # return 0
print(minStack.getMin()) # return -2