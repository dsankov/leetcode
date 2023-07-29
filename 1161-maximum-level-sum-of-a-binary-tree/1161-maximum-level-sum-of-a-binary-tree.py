# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        current_level = deque()
        current_level.append(root)

        sums = []
        while current_level:
            current_level_sum = 0    
            
            next_level = deque()
            while current_level:
                node = current_level.popleft()
                current_level_sum += node.val
                for child_node in (node.left, node.right):
                    if child_node:
                        next_level.append(child_node)
                        
            sums.append(current_level_sum)
            current_level = next_level

        max_sum = max(sums)
        return sums.index(max_sum) + 1

                