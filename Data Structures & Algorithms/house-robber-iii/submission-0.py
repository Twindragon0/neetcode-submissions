# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0,0] # [include, not include]
            leftRes = dfs(root.left)
            rightRes = dfs(root.right)
            return [root.val + leftRes[1] + rightRes[1], max(leftRes) + max(rightRes)]
        ans = dfs(root)
        return max(ans)