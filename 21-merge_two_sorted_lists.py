from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # takes care of edge cases
        # if a list is empty, return the other list
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        if list1.val <= list2.val:
            # If list1's value is smaller, it stays at the head
            # Recursively merge the rest of list1 and list2
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1  # Return list1 because it's the head of the merged list
        else:
            # If list2's value is smaller, it stays at the head
            # Recursively merge list1 and the rest of list2
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2  # Return list2 because it's the head of the merged list