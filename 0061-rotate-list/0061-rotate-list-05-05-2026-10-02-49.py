# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        n = 1
        start = head
        cur = start
        while cur.next:
            n += 1
            cur = cur.next

        k %= n
        if k == 0:
            return start

        cur.next = start
        cur = start
        while k > n:
            prev = cur
            cur = cur.next
            k += 1

        prev.next = None
        return cur
