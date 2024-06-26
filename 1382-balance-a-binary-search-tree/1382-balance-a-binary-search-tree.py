# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def get_inorder(root: TreeNode) -> list[int]:
            if not root:
                return None
            result = []
            if root.left:
                result.extend(get_inorder(root.left))
            result.append(root.val)
            if root.right:
                result.extend(get_inorder(root.right))
            return result

        def make_balanced_bst(inorder: list[int], left: int, right: int) -> TreeNode:
            if not inorder or left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(inorder[mid])
            root.left = make_balanced_bst(inorder, left, mid-1)
            root.right = make_balanced_bst(inorder, mid+1, right)
            return root

        inorder = get_inorder(root)
        result = make_balanced_bst(inorder, left=0, right=len(inorder)-1)

        return result

        