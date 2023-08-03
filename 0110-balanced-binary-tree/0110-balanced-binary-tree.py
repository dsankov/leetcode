# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _is_balanced_with_depth(self, root):
        if not root:
            return (True, 0)

        is_left_balanced,  left_depth  = self._is_balanced_with_depth(root.left)
        if not is_left_balanced:
            return (False, -1)
        
        is_right_balanced, right_depth = self._is_balanced_with_depth(root.right)
        if not is_right_balanced:
            return (False, -1)

        return (
            abs(left_depth - right_depth) <= 1,
            max(left_depth, right_depth) + 1
        )

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return self._is_balanced_with_depth(root)[0]

