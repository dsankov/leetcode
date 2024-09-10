# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_1 = head
        node_2 = node_1.next
        while node_2:
            mid_node = ListNode(val=math.gcd(node_1.val, node_2.val), next=node_2)
            node_1.next = mid_node
            node_1 = node_2
            node_2 = node_2.next
        return head
        