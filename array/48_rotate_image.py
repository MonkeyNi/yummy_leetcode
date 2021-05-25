class Solution:
    """
    Ref: 
    https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image
    https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)
    """
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # clockwise
        # top down flip, swap the symmetry 
        matrix[:] = map(list, zip(*matrix[::-1]))
        
        # anticlockwise
        # left right flip, swap the symmetry (or swap and then top down)
        matrix[:] = map(list, zip(*matrix))
        matrix[:] = matrix[::-1]