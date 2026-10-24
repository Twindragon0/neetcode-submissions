# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        queue = deque()
        queue.append((root, float("-inf")))
        while queue:
            node, maxSoFar = queue.popleft()
            if node.val >= maxSoFar:
                ans += 1
            if node.left:
                queue.append((node.left, max(maxSoFar, node.val)))
            if node.right:
                queue.append((node.right, max(maxSoFar, node.val)))
        return ans
            
