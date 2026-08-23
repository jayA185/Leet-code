class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)

        current = head

        while current:
            prev = dummy

            # Find correct position
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            next_node = current.next

            # Insert current
            current.next = prev.next
            prev.next = current

            current = next_node

        return dummy.next