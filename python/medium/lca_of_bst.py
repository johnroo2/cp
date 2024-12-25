class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAncestors(self, root: TreeNode, p: TreeNode, path):
        path.append(root)
        if root.val == p.val:
            return path
        elif root.val < p.val:
            return self.getAncestors(root.right, p, path)
        else:
            return self.getAncestors(root.left, p, path)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p1, p2 = self.getAncestors(root, p, []), self.getAncestors(root, q, [])

        for i in range(1, max(len(p1), len(p2))):
            if i >= min(len(p1), len(p2)) or p1[i].val != p2[i].val:
                return p1[i - 1]
        
