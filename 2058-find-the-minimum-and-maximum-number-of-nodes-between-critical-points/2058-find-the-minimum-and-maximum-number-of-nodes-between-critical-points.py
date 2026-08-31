# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_node = None
        cur_node = head
        next_node = head.next

        first_critical_id = cur_critical_id = None
        min_critical_distance = inf
        cur_node_id = 0

        while cur_node:
            cur_node_id += 1
            if not next_node:
                break

            if prev_node:
                prev_val = prev_node.val
                cur_val = cur_node.val
                next_val = next_node.val

                if prev_val < cur_val and cur_val > next_val or prev_val > cur_val and cur_val < next_val:
                    # print(cur_node_id, prev_val, cur_val, next_val)
                    if not first_critical_id:
                        first_critical_id = cur_node_id
                        prev_critical_id = cur_node_id
                    else:
                        cur_critical_id = cur_node_id
                        min_critical_distance = min(min_critical_distance, cur_critical_id - prev_critical_id)
                        prev_critical_id = cur_critical_id

            prev_node, cur_node, next_node = cur_node, next_node, next_node.next

        if not first_critical_id or not cur_critical_id or first_critical_id == cur_critical_id:
            return [-1, -1]

        return [min_critical_distance, cur_critical_id - first_critical_id]

                

        