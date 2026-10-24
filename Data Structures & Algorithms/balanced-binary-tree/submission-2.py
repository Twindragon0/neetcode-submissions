# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        height = 0
        stk = [root]
        visited = [False]
        nodeToHeight = defaultdict(int)
        while stk:
            node, v = stk.pop(), visited.pop()
            if node:
                if v:
                    leftHeight = nodeToHeight[node.left] if node.left else 0
                    rightHeight = nodeToHeight[node.right] if node.right else 0
                    nodeToHeight[node] = 1 + max(leftHeight, rightHeight)
                    if abs(leftHeight - rightHeight) > 1:
                        return False
                else:
                    stk.append(node)
                    stk.append(node.right)
                    stk.append(node.left)
                    visited.append(True)
                    visited.append(False)
                    visited.append(False)
        return True



        
