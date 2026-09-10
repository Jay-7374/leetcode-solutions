# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def solve(node):
            if node is None:
                return 0,0
            left,lcount = solve(node.left)
            right,rcount = solve(node.right)
            avg_sum = node.val + left + right
            avg_count = lcount +rcount + 1
            avg = avg_sum//avg_count
            if avg == node.val:
                self.count+=1
            return avg_sum,avg_count
        solve(root)
        return self.count
        