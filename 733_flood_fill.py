from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        basecolor = image[sr][sc]
        
        def help(image, sr, sc, basecolor):
        
            if not inarea(image, sr, sc):
                return
            if image[sr][sc] == -1:
                return
            if image[sr][sc] != basecolor:
                return
            
            image[sr][sc] = -1
            help(image, sr-1, sc, basecolor)
            help(image, sr+1, sc, basecolor)
            help(image, sr, sc-1, basecolor)
            help(image, sr, sc+1, basecolor)
            image[sr][sc] = newColor
            return
        
        def inarea(image, sr, sc):
            r = len(image)
            c = len(image[0])
            if sr < r and sr >= 0 and sc < c  and sc >= 0:
                return True
            return False
            
        help(image, sr, sc, basecolor)
        return image
    
test = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
res = test.floodFill(image, sr, sc, newColor)
for i in res:
    print(i)