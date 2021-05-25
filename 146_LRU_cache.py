from collections import OrderedDict


class LRUCache:
    """
    collections.OrderedDict: sorted dict
        popitem(last=True): True: LIFO, Flase: FIFO
        move_to_end(key): move key to the end (last in)
    """

    def __init__(self, capacity: int):
        self.size = capacity
        self.item = OrderedDict()
        

    def get(self, key: int):
        if key in self.item:
            self.item.move_to_end(key)
            return self.item[key]
        return -1
        

    def put(self, key: int, value: int):
        if not key in self.item and len(self.item) == self.size:
            self.item.popitem(last=False)
        self.item[key] = value
        self.item.move_to_end(key)

from collections import OrderedDict       
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.pool = OrderedDict()

    def get(self, key: int) -> int:
        if not key in self.pool:
            return -1
        else:
            self.pool.move_to_end(key)
            return self.pool[key]
        
    def put(self, key: int, value: int) -> None:
        # check size, if full, remove not used one
        if not key in self.pool and len(self.pool) == self.size:
            self.pool.popitem(last=False)
        self.pool[key] = value
        self.pool.move_to_end(key)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)