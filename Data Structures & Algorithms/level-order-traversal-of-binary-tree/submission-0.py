# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        ans = []
        queue.append(root)
        while queue:
            lst = []
            toPop = len(queue)
            for i in range(toPop):
                node = queue.popleft()
                lst.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(lst)
        return ans
