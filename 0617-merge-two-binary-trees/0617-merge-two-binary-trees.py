# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge_subtrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
            if not (root1 or root2):
                return None
            if root1 and root2:
                return TreeNode(val=root1.val+root2.val,
                                left=merge_subtrees(root1.left, root2.left),
                                right=merge_subtrees(root1.right, root2.right)
                                )
            if root1:
                return root1
            else:
                return root2

        return merge_subtrees(root1, root2)