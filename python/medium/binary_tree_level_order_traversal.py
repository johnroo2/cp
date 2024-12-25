
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = {}

        def rec(root, level):
            nonlocal mp

            if not root:
                return
            
            current = mp.get(level, [])
            current.append(root.val)

            mp[level] = current

            if root.left:
                rec(root.left, level + 1)
            if root.right:
                rec(root.right, level + 1)

        rec(root, 1)

        count = 1
        res = []

        while count in mp:
            res.append(mp[count])
            count += 1

        return res


