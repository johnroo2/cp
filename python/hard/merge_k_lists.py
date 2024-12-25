from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    head = ListNode(0)
    ptr = head

    while len([l for l in lists if l]) > 0:
        m = 1001
        mindex = -1
        for i, l in enumerate(lists):
            if l and l.val < m:
                m = l.val
                mindex = i
        
        ptr.next = ListNode(lists[mindex].val)
        ptr = ptr.next
        lists[mindex] = lists[mindex].next
    
    return head.next