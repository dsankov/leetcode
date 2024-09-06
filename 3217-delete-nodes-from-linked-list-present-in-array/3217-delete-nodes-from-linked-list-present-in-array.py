# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(next=head)
        current_node = dummy
        next_node = current_node.next
        while next_node:
            if next_node.val in nums:
                current_node.next = next_node.next
            else:
                current_node = current_node.next
            next_node = current_node.next

        return dummy.next            

        