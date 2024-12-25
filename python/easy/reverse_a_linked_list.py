from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    res = None

    while cur:
        res = ListNode(cur.val, res)
        cur = cur.next