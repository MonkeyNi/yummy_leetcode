from typing import List
from Union_find import Union_Find



class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # <= 1 will not work. Consider situation '[a!=a]'
        if len(equations) <= 0:
            return True
        
        UF = Union_Find(256)
        
        for ele in equations:
            if ele[1] != '!': 
                print(ord(ele[0]), ord(ele[-1]))
                UF.union(ord(ele[0]), ord(ele[-1]))
        
        print('check')
        for ele in equations:
            if ele[1] == '!':
                print(ord(ele[0]), ord(ele[-1]))
                if UF.connected(ord(ele[0]), ord(ele[-1])):
                    return False
                
        return True
    
    
test = Solution()
equs = ["a==b","b!=a"]
equs = ["b==a","a==b"]
equs = ["a==b","b==c","a==c"] # True
equs = ["a==b","b!=c","c==a"] # False
equs = ["c==c","b==d","x!=z"] # True
equs = ["a!=a"]
res = test.equationsPossible(equs)
print(res)