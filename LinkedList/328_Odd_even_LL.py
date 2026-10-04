# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return
        odd=head
        even=head.next
        evenstart=head.next
        while(even is not None and even.next is not None):
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenstart
        return head



time comp:O(n)
space comp:O(1)
