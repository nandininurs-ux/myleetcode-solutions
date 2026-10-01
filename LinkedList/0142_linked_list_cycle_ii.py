class Solution:
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None

        slow = fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if slow != fast:
            return None

        p = head

        while p != slow:
            p = p.next
            slow = slow.next

        return p
