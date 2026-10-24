# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root, maxSoFar):
            if not root:
                return
            if root.val >= maxSoFar:
                self.ans += 1
            dfs(root.left, max(maxSoFar, root.val))
            dfs(root.right, max(maxSoFar, root.val))
        dfs(root, float("-inf"))
        return self.ans
            
