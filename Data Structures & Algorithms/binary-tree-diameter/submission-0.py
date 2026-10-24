# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            leftRoot = dfs(root.left)
            rightRoot = dfs(root.right)
            self.ans = max(self.ans, leftRoot+rightRoot+1)
            return 1 + max(leftRoot, rightRoot)
        dfs(root)
        return self.ans-1
