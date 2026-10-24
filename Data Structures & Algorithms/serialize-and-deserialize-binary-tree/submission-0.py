# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        myStr = ""
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            myStr += str(node.val) + "a" if node else "nulla"
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return myStr

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        queue = deque()
        root = TreeNode(int(data[:data.index("a")]))
        queue.append(root)

        data = data[data.index("a")+1:]
        while data:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()

                leftVal = data[:data.index("a")]
                data = data[data.index("a")+1:]
                rightVal = data[:data.index("a")]
                data = data[data.index("a")+1:]

                node.left = TreeNode(int(leftVal)) if leftVal != "null" else None
                node.right = TreeNode(int(rightVal)) if rightVal != "null" else None

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
