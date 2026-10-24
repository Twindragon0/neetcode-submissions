# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p, q))
        while queue:
            currP, currQ = queue.popleft()
            if not currP and not currQ:
                continue
            if not currP or not currQ:
                return False
            if currP.val != currQ.val:
                return False
            queue.append((currP.left, currQ.left))
            queue.append((currP.right, currQ.right))
        return True

