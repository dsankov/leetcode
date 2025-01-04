# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_val_queue = []
        node_id = 0
        for root in lists:
            if not root:
                continue
            min_val_queue.append((root.val, node_id, root.next))
            node_id += 1

        heapify(min_val_queue)
        if not min_val_queue:
            return None

        root = ListNode()
        node = root
        while min_val_queue:
            min_val, _, next_node = heappop(min_val_queue)
            node.val = min_val
            if next_node:
                heappush(min_val_queue, (next_node.val, node_id, next_node.next))
                node_id += 1
            if min_val_queue:
                node.next = ListNode()
                node = node.next
        return root

        