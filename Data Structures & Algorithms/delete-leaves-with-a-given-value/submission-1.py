# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]
        visited = [False]
        nodeToRemove = defaultdict(bool)
        while stack:
            node, v = stack.pop(), visited.pop()
            if v:
                node.left = None if not node.left or nodeToRemove[node.left] else node.left
                node.right = None if not node.right or nodeToRemove[node.right] else node.right
                if not node.left and not node.right and node.val == target:
                    nodeToRemove[node] = True
            else:
                stack.append(node)
                visited.append(True)
                if node.right:
                    stack.append(node.right)
                    visited.append(False)
                if node.left:
                    stack.append(node.left)
                    visited.append(False)
        return root if not nodeToRemove[root] else None
        

        