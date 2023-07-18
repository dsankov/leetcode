# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        root = head
        even_root = head.next
        odd = root 
        even = even_root
        if not even:
            return root

        while True:
            if not odd:
                odd = even_root
                break
            if not even or not even.next:
                odd.next = even_root
                break

            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next       
  
        return root