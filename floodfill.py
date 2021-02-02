from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        startcolor = image[sr][sc]
        self.dfs(sr, sc, startcolor, newColor, image)
        return image

    def dfs(self, x, y, startcolor, newcolor, image):
        # over boundary
        if not self.inarea(image, x, y):
            return
        # not same color
        if image[x][y] != startcolor:
            return
        # if image[x][y] == -1:
        #     return
        # avoid duplicate visit
        image[x][y] = -1
        self.dfs(x-1, y, startcolor, newcolor, image)
        self.dfs(x+1, y, startcolor, newcolor, image)
        self.dfs(x, y-1, startcolor, newcolor, image)
        self.dfs(x, y+1, startcolor, newcolor, image)
        image[x][y] = newcolor
        return

    def inarea(self, image, x, y):
        if x >=0 and x < len(image) and \
            y >=0 and y < len(image[0]):
            return True

test = Solution()
image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2
res = test.floodFill(image, sr, sc, newColor)
print(res)