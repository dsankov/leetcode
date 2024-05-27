# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirrored(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not(left and right):
                return False
            if left.val != right.val:
                return False
            return is_mirrored(left.left, right.right) and is_mirrored(left.right, right.left)
            

        if not root:
            return True
        return is_mirrored(root.left, root.right)
        