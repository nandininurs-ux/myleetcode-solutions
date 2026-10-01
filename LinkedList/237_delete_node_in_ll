class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def deleteNode(self, node):
         current=node
         while(current.next.next!=None):
              current.val=current.next.val
              current=current.next
         current.val=current.next.val
         current.next=None


time complexity:O(1)
space complexity:O(1)
