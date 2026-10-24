# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        visited = [False]
        stack = [root]
        nodeToVal = defaultdict(int)
        nodeToVal[None] = 0
        ans = 0
        while stack:
            node, v = stack.pop(), visited.pop()
            if v:
                nodeToVal[node] = 1 + max(nodeToVal[node.left], nodeToVal[node.right])
                ans = max(ans, 1 + nodeToVal[node.left] + nodeToVal[node.right])
            else:
                stack.append(node)
                visited.append(True)
                if node.right:
                    stack.append(node.right)
                    visited.append(False)
                if node.left:
                    stack.append(node.left)
                    visited.append(False)
        return ans-1
