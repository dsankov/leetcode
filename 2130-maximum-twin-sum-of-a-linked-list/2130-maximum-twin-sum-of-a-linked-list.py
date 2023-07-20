# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = -1
        values = []
        test_node = head
        while test_node:
            values.append(test_node.val)
            test_node = test_node.next
            
        n = len(values)
        for i in range(n // 2):
            max_sum = max(max_sum, values[i]+values[n-1 - i])

        return max_sum
            

        