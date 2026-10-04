# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current=head
        len=0
        while(current!=None):
         len=len+1
         current=current.next
        p1=head
        count=k
        while(count>1):
          p1=p1.next
          count=count-1
        p2=head
        s=len-k+1
        while(s>1):
         p2=p2.next
         s=s-1
        p1.val,p2.val=p2.val,p1.val
        return head


time complexity: O(n)
space : O(1)
