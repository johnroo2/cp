from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(self, root: Optional[TreeNode]) -> bool:
    mp = { None: 0 }
    stack = []  

    stack.append(root)

    while stack:
        node = stack[-1]
        if not node:
            stack.pop()
            continue

        if (node.left in mp) and (node.right in mp):
            stack.pop()
            left_height = mp.get(node.left, -1) 
            right_height = mp.get(node.right, -1) 
            if abs(mp[node.left] - mp[node.right]) > 1:
                return False
            mp[node] = max(left_height, right_height) + 1 
        else:
            if node.right and node.right not in mp:
                stack.append(node.right)
            if node.left and node.left not in mp:
                stack.append(node.left)

    return True
    

        

    