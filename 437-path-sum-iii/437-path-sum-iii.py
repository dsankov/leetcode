# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def sub_path_sum(root: TreeNode, target_sum: int, start_from_here: bool) -> int:

            if not root:
                return 0

            target_sum -= root.val
            result = 1 if target_sum == 0 else 0
            
            if start_from_here:         # use global targetSum
                result += sub_path_sum(root.left,  targetSum, start_from_here=True)
                result += sub_path_sum(root.right, targetSum, start_from_here=True)

            result += sub_path_sum(root.left,  target_sum, start_from_here=False)
            result += sub_path_sum(root.right, target_sum, start_from_here=False)

            return result

        return sub_path_sum(root, targetSum, start_from_here=True)
