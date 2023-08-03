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
            # print(f'step:{step_number}\t1_step ptr: {forward_1_step.val}\t2_step ptr: {forward_2_steps.val}')

            forward_2_steps = forward_2_steps.next.next
            forward_1_step = forward_1_step.next
            
            if forward_1_step == forward_2_steps:
                # print(f'cycle found at\nstep:{step_number}\t1_step fin: {forward_1_step.val}\t2_step fin: {forward_2_steps.val}')
                return True
            step_number += 1
        
        return False


        # visited_nodes = []
        # pointer = head
        # while pointer and pointer not in visited_nodes:
        #     visited_nodes.append(pointer)
        #     pointer = pointer.next
            
        # return pointer is not None