# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _dfs_count(self, root: TreeNode, count_leaves_distance: list[int]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            count_leaves_distance[0] = 1
            return 0
        left_leaves  = [0] * (self.distance + 1)
        right_leaves = [0] * (self.distance + 1)

        left_pairs  = self._dfs_count(root.left, left_leaves)
        right_pairs = self._dfs_count(root.right, right_leaves)
        cross_pairs = 0

        for distance in range(self.distance):
            count_leaves_distance[distance + 1] = left_leaves[distance] + right_leaves[distance]     
        
        for left_distance in range(self.distance):
            for right_distance in range(self.distance - (left_distance + 1)):
                cross_pairs += left_leaves[left_distance] * right_leaves[right_distance]

        return cross_pairs + left_pairs + right_pairs

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.distance = distance
        count_leaves_distance = [0] * (self.distance + 1)
        return self._dfs_count(root, count_leaves_distance)


        