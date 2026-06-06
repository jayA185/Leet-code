class Solution:
    def reverseKGroup(self, head, k):
        def reverse(start, end):
            prev = end
            while start != end:
                nxt = start.next
                start.next = prev
                prev = start
                start = nxt
            return prev

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            start = group_prev.next

            group_prev.next = reverse(start, group_next)
            group_prev = start