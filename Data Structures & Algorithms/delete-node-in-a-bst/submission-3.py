# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        prev = None
        curr = root
        while curr:
            if key < curr.val:
                prev = curr
                curr = curr.left
            elif key > curr.val:
                prev = curr
                curr = curr.right
            else:
                break
        
        if not curr:
            return root
        if not curr.left or not curr.right:
            if not prev:
                root = curr.right if not curr.left else curr.left
            elif prev.left == curr:
                prev.left = curr.right if not curr.left else curr.left
            else:
                prev.right = curr.right if not curr.left else curr.left
        else:
            leftOfRightSubtree = curr.right
            while leftOfRightSubtree.left:
                leftOfRightSubtree = leftOfRightSubtree.left
            leftOfRightSubtree.left = curr.left
            toAdd = curr.right
            if not prev:
                root = toAdd
            elif prev.left == curr:
                prev.left = toAdd
            else:
                prev.right = toAdd
        return root
            

    
        

