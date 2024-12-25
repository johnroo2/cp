from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(self, head: Optional[ListNode]) -> None:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    res, cur = None, slow.next
    slow.next = None
    while cur:
        temp = cur.next
        cur.next = res
        res = cur
        cur = temp
        
    first, second = head, res
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2