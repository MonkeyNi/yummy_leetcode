class Union_Find:
    """
    并查集，解决动态连通性问题
    """
    
    def __init__(self, n):
        self.N = n
        self.parents = [i for i in range(n)]
        # Purpose of size: connect small tree to big tree (keep smaller tree height)
        self.sizes = [1 for _ in range(n)]
        self.count = n
        
    def union(self, p, q):
        """
        Connect two nodes
        """
        if not self.check_exist(p) or not self.check_exist(q):
            print('Invalid input.')
            return
        
        parent_p = self.find(p)
        parent_q = self.find(q)
        if parent_p == parent_q:
            return
        if self.sizes[parent_p] > self.sizes[parent_q]:
            self.parents[parent_q] = parent_p
            self.sizes[parent_p] += self.sizes[parent_q]
        else:
            self.parents[parent_q] = parent_p
            self.sizes[parent_q] += self.sizes[parent_p]
        self.count -= 1
    
    def connected(self, p, q):
        """
        Checkt if p and q are connected
        """
        if not self.check_exist(p) or not self.check_exist(q):
            print('Invalid input.')
            return False
        
        return self.find(p) == self.find(q)
    
    def find(self, p):
        """
        Find root
        """
        if not self.check_exist(p):
            print('Invalid input.')
            return -1
        
        while self.parents[p] != p:
            # compress tree, to make find time complexity O(1)
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    
    def _count(self,):
        """
        Number of connected components
        """
        return self.count
    
    def check_exist(self, p):
        if p >=0  and p < self.N:
            return True
        else:
            return False
    

# test = Union_Find(n=10)
# print(test._count()) # 10
# print(test.connected(0,1)) # false
# print(test.connected(3,9)) # false
# print(test.find(1)) # 1
# print(test.find(10)) # -1
# print(test.union(2, 4)) # None
# print(test.connected(2, 4)) # True
# print(test._count()) # 9