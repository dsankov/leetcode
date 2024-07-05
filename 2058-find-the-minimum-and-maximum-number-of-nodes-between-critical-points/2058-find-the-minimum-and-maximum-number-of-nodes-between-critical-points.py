# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_node = head
        last_extremum_index = 0
        min_seen_interval = float("inf")
        cur_node = head.next
        cur_index = 1
        while cur_node.next:
            if prev_node.val < cur_node.val > cur_node.next.val \
                or prev_node.val > cur_node.val < cur_node.next.val:
                    if last_extremum_index == 0:
                        last_extremum_index = cur_index
                        first_extremum_index = cur_index
                    else:
                        min_seen_interval = min(min_seen_interval,
                                                cur_index - last_extremum_index)
                        last_extremum_index = cur_index
            prev_node = cur_node
            cur_index += 1
            cur_node = cur_node.next
        if min_seen_interval == float("inf"):
            return [-1, -1]
        else:
            return [min_seen_interval, last_extremum_index - first_extremum_index]
        
