class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def rec(t, m):
            nonlocal res 

            if not t:
                return

            if t.val >= m:
                res += 1
            
            rec(t.right, max(t.val, m))
            rec(t.left, max(t.val, m))

        rec(root, float("-inf"))

        return res

            