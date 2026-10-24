# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorderMap = defaultdict(int)
        for idx, val in enumerate(inorder):
            self.inorderMap[val] = idx
        
        def recurse(pL, pR, iL, iR):
            if pL > pR or iL > iR:
                return None
            root = TreeNode(preorder[pL])
            idx = self.inorderMap[root.val]
            root.left = recurse(pL+1, pL+(idx-iL), iL, idx-1)
            root.right = recurse(pL+(idx-iL)+1, pR, idx+1, iR)
            return root
        return recurse(0, len(preorder)-1, 0, len(inorder)-1)