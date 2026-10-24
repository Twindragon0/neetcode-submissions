# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            toPop = len(queue)
            lastNode = None
            for i in range(toPop):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                lastNode = node
            ans.append(lastNode.val)
        return ans

        