class TreeNode:
    """[summary]
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def build_tree(nums):
    if not nums:
        return None
    i_r, i_l, i_rh = 0, 1, 2
    nodes = [TreeNode(val=num) if num else TreeNode(val=0) for num in nums]
    while i_rh < len(nums):
        if nums[i_r]:
            nodes[i_r].left = nodes[i_l]
            nodes[i_r].right = nodes[i_rh]
            i_l += 2
            i_rh += 2
        i_r += 1
    return nodes[0]
    