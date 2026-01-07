# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.subtree_sums = []
        def build_subtree_sums_dfs(root: TreeNode | None) -> int:
            if not root:
                return 0
            left_sum = build_subtree_sums_dfs(root.left)
            if left_sum > 0:
                self.subtree_sums.append(left_sum)
            right_sum = build_subtree_sums_dfs(root.right)
            if right_sum > 0:
                self.subtree_sums.append(right_sum)

            return left_sum + right_sum + root.val

        total_sum = build_subtree_sums_dfs(root)
        max_product = 0
        for subtree_sum in self.subtree_sums:
            max_product = max(max_product, subtree_sum * (total_sum - subtree_sum))
        return max_product % (10**9 + 7)