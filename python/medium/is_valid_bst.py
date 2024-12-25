from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mp = {None: (float("-inf"), float("inf"))}

        stack = [root]

        while stack:
            node = stack.pop()

            if node in mp:
                continue
            elif node.left in mp and node.right in mp:
                mp[node] = (max(mp[node.left][0], mp[node.right][0], node.val), 
                min(mp[node.left][1], mp[node.right][1], node.val))
            else:
                stack.append(node)
                if node.left not in mp:
                    stack.append(node.left)
                if node.right not in mp:
                    stack.append(node.right)

        def rec (t):
            nonlocal mp

            if not t: 
                return True
            left = float("-inf") if not t.left else mp[t.left][0]
            right = float("inf") if not t.right else mp[t.right][1]
            
            return t.val > left and t.val < right and rec(t.left) and rec(t.right)
        
        return rec (root)