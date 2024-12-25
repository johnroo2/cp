from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    res = ListNode(0)
    ptr = res

    while l1 and l2:
        ptr.next = ListNode(0)
        ptr = ptr.next
        digit_sum = l1.val + l2.val + carry
        if digit_sum >= 10:
            carry = 1
            digit_sum -= 10
        else:
            carry = 0
        ptr.val = digit_sum
        l1 = l1.next
        l2 = l2.next

    rem = l1 if l1 else l2

    while rem or carry == 1:
        if carry == 1 and not rem:
            ptr.next = ListNode(1)
            break
        ptr.next = ListNode(0)
        ptr = ptr.next
        digit_sum = rem.val + carry
        if digit_sum >= 10:
            carry = 1
            digit_sum -= 10
        else:
            carry = 0
        ptr.val = digit_sum
        rem = rem.next

    return res.next