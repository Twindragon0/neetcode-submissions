# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca = None

        def recurse(root, p, q):
            if not root:
                return [False, False]
            left = recurse(root.left, p, q)
            right = recurse(root.right, p, q)

            x = left[0] or right[0] or root == p
            y = left[1] or right[1] or root == q
            if x and y and not self.lca:
                self.lca = root
            return [x, y]
        recurse(root, p, q)
        return self.lca
