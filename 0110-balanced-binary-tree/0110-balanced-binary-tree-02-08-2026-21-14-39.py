# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _is_balanced(self, node: TreeNode | None) -> tuple[bool, int]:
        if not node:
            return (True, -1)

        left_balanced, left_depth = self._is_balanced(node.left)
        if not left_balanced:
            return (False, 0)
        right_balanced, right_depth = self._is_balanced(node.right)
        if not right_balanced:
            return (False, 0)
            
        return (abs(left_depth - right_depth) <= 1, 1 + max(left_depth, right_depth))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._is_balanced(root)[0]

        