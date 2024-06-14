# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap_pair(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return None
            next_item = head.next
            if not next_item:
                return head
            tail = next_item.next
            swapped_tail = swap_pair(tail)
            head.next = swapped_tail
            next_item.next = head
            return next_item

        return swap_pair(head) 
        