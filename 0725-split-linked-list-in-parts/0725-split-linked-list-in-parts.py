# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        current_node = head
        while current_node:
            size += 1
            current_node = current_node.next

        split_size, extra_nodes = divmod(size, k)
        result = [None] * k
        current_global_node = head
        for i in range(k):
            new_part_dummy_begining = ListNode()
            current_part_node = new_part_dummy_begining
            current_size = split_size + (1 if i < extra_nodes else 0)
            for j in range(current_size):
                current_part_node.next = ListNode(val=current_global_node.val)
                current_part_node = current_part_node.next
                current_global_node = current_global_node.next
            
            result[i] = new_part_dummy_begining.next

        return result
        