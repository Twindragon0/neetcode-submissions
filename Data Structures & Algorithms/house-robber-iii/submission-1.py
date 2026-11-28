# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def recurse(root):
            if not root:
                return 0, 0
            noLeft, yesLeft = recurse(root.left)
            noRight, yesRight = recurse(root.right)
            return max(noLeft, yesLeft) + max(noRight, yesRight), root.val + noLeft + noRight
        l, r = recurse(root)
        return max(l, r)