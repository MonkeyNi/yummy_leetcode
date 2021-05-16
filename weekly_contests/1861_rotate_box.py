from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        if not len(box) or not (len(box[0])):
            return box
        
        # rotate box
        def rot_box(box):
            x, y = len(box[0]), len(box)
            rot = [['*']*y for _ in range(x)]
            for i in range(y):
                for j in range(x):
                    _i = j
                    _j = y - 1 - i
                    rot[_i][_j] = box[i][j]
            return rot
        
        # remove all to the right
        def move_right(nums):
            start = 0
            for i, n in enumerate(nums):
                if n == '#':
                    continue
                elif n == '.':
                    nums[start], nums[i] = nums[i], nums[start]
                    start += 1
                elif n == '*':
                    start = i + 1
            return nums
        
        for i in range(len(box)):
            box[i] = move_right(box[i])
        return rot_box(box)