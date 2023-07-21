# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good_nodes(root: TreeNode, max_node: int) -> int:
            if not root:
                return 0
  
            if root.val >= max_node:
                return (1 +
                    good_nodes(root.left, root.val) +
                    good_nodes(root.right, root.val)
                )
            else:
                return (0 +
                    good_nodes(root.left, max_node) +
                    good_nodes(root.right, max_node)
                )

        return good_nodes(root, -math.inf)