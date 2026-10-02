# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return 
        if head.next is None:
            return head
        if head.next.next is None:
            head=head.next
            head.next=None
            return head
        slow,fast=head,head
        while(fast and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow
