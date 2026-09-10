# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> list[int]:
            if not node:
                return [0, 0, 0]
            left_node_count, left_sum, left_good_count = dfs(node.left)
            right_node_count, right_sum, right_good_count = dfs(node.right)
            node_good_count = left_good_count + right_good_count
            if (node.val + left_sum + right_sum) // (1 + left_node_count + right_node_count) == node.val:
                node_good_count += 1
            return [(1 + left_node_count + right_node_count), (node.val + left_sum + right_sum), node_good_count]
        
        return dfs(root)[2]