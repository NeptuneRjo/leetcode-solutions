from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current:
            # if the next value is the same as the current value-
            # set the current value to the next, overwriting it.
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            current = current.next
        return head
                
    