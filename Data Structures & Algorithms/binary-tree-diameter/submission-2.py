# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def recurse(root):
            if not root:
                return 0
            left = recurse(root.left)
            right = recurse(root.right)
            self.diameter = max(self.diameter, 1 + left + right)
            return 1 + max(left, right)
        recurse(root)
        return self.diameter-1