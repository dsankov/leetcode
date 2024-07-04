# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        read = head.next
        write = head
        prev = write
        cumulative_sum = 0
        while read:
            if read.val != 0:
                cumulative_sum += read.val
            else:
                write.val = cumulative_sum
                cumulative_sum = 0
                prev = write
                write = write.next
            read = read.next
        prev.next = None
        return dummy
        