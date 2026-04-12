class Solution(object):
    def reorderList(self, head):
        if not head or not head.next: return       
        # find middle
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next       
        # reverse second half
        prev, cur = None, slow.next
        slow.next = None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next   
        # merge two halves
        first, second = head, prev
        while second:
            first.next, first = second, first.next
            second.next, second = first, second.next     