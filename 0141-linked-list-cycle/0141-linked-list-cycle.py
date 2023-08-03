# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        forward_1_step, forward_2_steps = head, head
        step_number = 0
        
        while forward_2_steps and forward_2_steps.next:

            forward_2_steps = forward_2_steps.next.next
            forward_1_step = forward_1_step.next
            
            if forward_1_step == forward_2_steps:

                return True
            step_number += 1
        
        return False
