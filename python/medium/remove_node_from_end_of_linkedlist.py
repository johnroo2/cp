from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    first, second = head, dummy

    for _ in range(n):
        first = first.next

    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next

    return dummy.next