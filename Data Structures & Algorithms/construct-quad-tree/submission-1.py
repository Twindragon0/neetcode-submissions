"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        if n == 1:
            return Node(grid[0][0], 1, None, None, None, None)
        node = Node(grid[0][0], 0, None, None, None, None)
        topLeft = self.construct([el[:n//2] for el in grid[:n//2]])
        topRight = self.construct([el[n//2:] for el in grid[:n//2]])
        bottomLeft = self.construct([el[:n//2] for el in grid[n//2:]])
        bottomRight = self.construct([el[n//2:] for el in grid[n//2:]])
        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
            node.isLeaf = 1
        else:
            node.topLeft = topLeft
            node.topRight = topRight
            node.bottomLeft = bottomLeft
            node.bottomRight = bottomRight
        return node
        