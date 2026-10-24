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
        
        def recurse(preRootIdx, lim, inMin):
            if preRootIdx > lim:
                return None
            root = TreeNode(preorder[preRootIdx])
            rootIdx = self.inorderMap[root.val]
            root.left = recurse(preRootIdx+1, preRootIdx+(rootIdx-inMin), inMin)
            root.right = recurse(preRootIdx+(rootIdx-inMin)+1, lim, rootIdx+1)
            return root
        return recurse(0, len(preorder)-1, 0)