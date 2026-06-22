# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find_mins(node, k):
            if not node:
                return (0, None)
            left_mins, k_min = find_mins(node.left, k)
            if k_min is not None:
                return (0, k_min) 
            k -= left_mins
            k -= 1
            if k == 0:
                return (0, node.val)
            right_mins, k_min = find_mins(node.right, k)
            if k_min is not None:
                return (0, k_min)
            
            return (left_mins + 1 + right_mins, None)
              
        return find_mins(root, k)[1]

