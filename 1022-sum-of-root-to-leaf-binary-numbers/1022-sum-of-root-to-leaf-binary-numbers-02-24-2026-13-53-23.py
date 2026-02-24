# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, path):
            nonlocal total
            if not node.left and not node.right:
                total += (path << 1) + node.val
                return

            if node.left:
                dfs(node.left, (path<<1) + node.val)
            if node.right:
                dfs(node.right, (path<<1) + node.val)

        dfs(root, 0)
        return total