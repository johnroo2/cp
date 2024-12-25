from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
    copymap = {None: None}

    cur = head
    while cur:
        if cur not in copymap:
            copymap[cur] = Node(0)
        if cur.next not in copymap:
            copymap[cur.next] = Node(0)
        if cur.random not in copymap:
            copymap[cur.random] = Node(0)
        copymap[cur].val = cur.val
        copymap[cur].next = copymap[cur.next]
        copymap[cur].random = copymap[cur.random]
        cur = cur.next
    
    return copymap[head]