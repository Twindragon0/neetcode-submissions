# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        def dfs(root):
            if not root:
                return 0
            leftLeaf = dfs(root.left)
            rightLeaf = dfs(root.right)
            #root.val, root.val + leftLeaf + rightLeaf, root.val + leftLeaf, root.val + rightLeaf
            self.ans = max(self.ans, root.val, root.val + leftLeaf + rightLeaf, root.val + leftLeaf, root.val + rightLeaf)
            return root.val + max(0, max(leftLeaf, rightLeaf))
        dfs(root)
        return self.ans
