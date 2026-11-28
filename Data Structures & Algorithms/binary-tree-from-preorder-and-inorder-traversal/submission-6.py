# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.numToIdx = defaultdict(int)
        for i, el in enumerate(inorder):
            self.numToIdx[el] = i
        def recurse(preLo, preHi, inLo, inHi):
            # print("lo: " + str(lo) + ", hi: " + str(hi))
            if preLo > preHi:
                return None
            root = TreeNode(preorder[preLo])
            numLeft, numRight = self.numToIdx[preorder[preLo]] - inLo, inHi - self.numToIdx[preorder[preLo]]
            root.left = recurse(preLo+1, preLo+numLeft, inLo, self.numToIdx[preorder[preLo]] - 1)
            root.right = recurse(preLo+numLeft+1, preLo+numLeft+numRight, self.numToIdx[preorder[preLo]] + 1, inHi)
            return root
        return recurse(0, len(preorder)-1, 0, len(inorder)-1)