# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ans = root
        def recurse(root, p, q):
            if not root:
                return 0
            left = recurse(root.left, p, q)
            right = recurse(root.right, p, q)
            val = 1 if root == p or root == q else 0
            if left == 2 or right == 2:
                return 2
            elif val+left+right == 2:
                self.ans = root
                return 2
            else:
                return val+left+right
        recurse(root, p, q)
        return self.ans
