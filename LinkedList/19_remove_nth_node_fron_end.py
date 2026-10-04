# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head is None:
            return
        current=head
        sum=0
        while(current!=None):
            sum=sum+1
            current=current.next
        count=sum-n+1
        p=head
        if (count==1):
            return head.next
        else:
           while(count>2):
            p=p.next
            count=count-1
           p.next=p.next.next

        return head

time complexity:O(n)
space complexity: O(1)
