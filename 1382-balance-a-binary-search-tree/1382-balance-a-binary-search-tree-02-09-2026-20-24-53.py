# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_inorder(self, node):
        if not node:
            return
        self.build_inorder(node.left)
        self.inorder.append(node.val)
        self.build_inorder(node.right)
    
    def build_balanced(self, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        node = TreeNode(self.inorder[mid])
        node.left = self.build_balanced(start, mid - 1)
        node.right = self.build_balanced(mid + 1, end)
        return node

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.inorder = []
        self.build_inorder(root)
        return self.build_balanced(0, len(self.inorder) - 1)