class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # 1. Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3. Merge two halves
        first = head
        second = prev

        while second:
            firstNext = first.next
            secondNext = second.next

            first.next = second
            second.next = firstNext

            first = firstNext
            second = secondNext