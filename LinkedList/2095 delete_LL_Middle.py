 def deleteMiddle(head):
          if head is None:
            return 
          if head.next is None:
            return None
          if head.next.next is None:
            head.next=None
            return head
          slow,fast=head,head
          while(fast and fast.next is not None):
            slow=slow.next
            fast=fast.next.next
          current=slow
          while(current.next.next is not None):
            current.val=current.next.val
            current=current.next
          current.val=current.next.val
          current.next=None
          return head
