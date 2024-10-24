# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def cmp_nodes_val(node1: TreeNode | None, node2: TreeNode | None) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val

        nodes_pairs_stack = [(root1, root2)]
        while nodes_pairs_stack:
            node1, node2 = nodes_pairs_stack.pop()
            if not node1 and not node2:
                continue
            if not cmp_nodes_val(node1, node2):
                return False
            if cmp_nodes_val(node1.left, node2.left):
                nodes_pairs_stack.append((node1.left, node2.left))
                nodes_pairs_stack.append((node1.right, node2.right))
            else:
                nodes_pairs_stack.append((node1.left, node2.right))
                nodes_pairs_stack.append((node1.right, node2.left))
        return True