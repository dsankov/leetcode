# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def greater_tree(root: TreeNode, greater_sum: int) -> int:
            if not root:
                return greater_sum
            right_sum = greater_tree(root.right, greater_sum)
            left_sum = greater_tree(root.left, 
                                    greater_sum=right_sum+root.val
                                    )
            root.val = right_sum + root.val
            return left_sum

        greater_tree(root, greater_sum=0)
        return root
        