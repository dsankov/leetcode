# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSameSubTree(p, q):
            if not p and q or p and not q:
                return False
            if not p and not q:
                return True
            return p.val == q.val and isSameSubTree(p.right, q.right) and isSameSubTree(p.left, q.left)
        
        return isSameSubTree(p, q)
        