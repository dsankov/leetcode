# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        current_node = head
        while current_node:
            while current_node.next and current_node.next.val in nums:
                current_node.next = current_node.next.next
            current_node = current_node.next
        if head.val in nums:
            head = head.next

        return head         

        