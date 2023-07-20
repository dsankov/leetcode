# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = -math.inf
        n = 1
        test_node = head
        reversed_list = None
        while test_node:
            temp = ListNode(val = test_node.val)
            temp.next = reversed_list
            reversed_list = temp
            test_node = test_node.next
            n += 1
        test_node = head
        reversed_node = reversed_list
        for _ in range(n//2):
            max_sum = max(max_sum, test_node.val + reversed_node.val)
            test_node = test_node.next
            reversed_node = reversed_node.next
        return max_sum
            

        