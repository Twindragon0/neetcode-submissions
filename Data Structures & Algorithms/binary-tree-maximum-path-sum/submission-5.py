# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        def recurse(root):
            if not root:
                return 0
            leftLongest = recurse(root.left)
            rightLongest = recurse(root.right)
            toRet = max(root.val, root.val + leftLongest, root.val + rightLongest)
            self.ans = max(self.ans, toRet, leftLongest + root.val + rightLongest)
            return toRet
        recurse(root)
        return self.ans