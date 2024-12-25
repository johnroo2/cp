from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            if not node:
                return "(-)"
            return f"({node.val})"+preorder(node.left)+preorder(node.right)

        return preorder(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = [token for token in data[1:-1].split(")(")]

        def build_tree():
            if not tokens:
                return None
            val = tokens.pop(0)
            if val == "-":
                return None
            node = TreeNode(int(val), build_tree(), build_tree())
            return node

        return build_tree()