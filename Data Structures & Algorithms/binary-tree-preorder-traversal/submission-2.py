# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = []
        ans = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                ans.append(curr.val)
                curr = curr.left
            node = stack.pop()
            curr = node.right
        return ans
