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
    def isUnique(self, grid):
        els = set()
        for row in grid:
            for col in row:
                els.add(col)
                if len(els) == 2:
                    return False
        return True
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        print(grid)
        if self.isUnique(grid):
            return Node(grid[0][0], 1, None, None, None, None)
        node = Node(grid[0][0], 0, None, None, None, None)
        node.topLeft = self.construct([el[:n//2] for el in grid[:n//2]])
        node.topRight = self.construct([el[n//2:] for el in grid[:n//2]])
        node.bottomLeft = self.construct([el[:n//2] for el in grid[n//2:]])
        node.bottomRight = self.construct([el[n//2:] for el in grid[n//2:]])
        return node
        