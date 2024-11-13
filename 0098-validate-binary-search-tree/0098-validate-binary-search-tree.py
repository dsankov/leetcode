# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_bound, max_bound):
            if not node:
                return True
            if not min_bound < node.val < max_bound:
                return False
                
            return (
                dfs(node.left, min_bound, min(node.val, max_bound)) 
                and dfs(node.right, max(node.val, min_bound), max_bound)
            )

        return dfs(root, -math.inf, math.inf)

        