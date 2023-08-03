# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer, slow_pointer = head, head
        step = 1
        while pointer:
            if step % 2 == 0:
                slow_pointer = slow_pointer.next
            step += 1
            pointer = pointer.next
            
        return slow_pointer