from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    count = 0
    cur = head
    while cur and count < k:
        cur = cur.next
        count += 1
    
    if count == k:
        cur = self.reverseKGroup(cur, k)
        while count > 0:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
            count -= 1
        head = cur

    return head