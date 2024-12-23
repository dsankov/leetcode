# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        nodes_queue = deque([root])
        total_swaps = 0
        while nodes_queue:
            level_size = len(nodes_queue)
            curr_level = []
            for _ in range(level_size):
                curr_node = nodes_queue.popleft()
                curr_level.append(curr_node.val)
                if curr_node.left:
                    nodes_queue.append(curr_node.left)
                if curr_node.right:
                    nodes_queue.append(curr_node.right)
            total_swaps += self.count_swaps(curr_level)
        return total_swaps

    def count_swaps(self, nums):
        sorted_nums = sorted(nums)
        index_of_num = {num:idx for idx, num in enumerate(nums)}
        swaps = 0

        for position, num in enumerate(nums):
            correct_num = sorted_nums[position]
            if num == correct_num:
                continue
            swaps += 1
            position_of_correct_num = index_of_num[correct_num]
            nums[position_of_correct_num] = num
            index_of_num[num] = position_of_correct_num

        return swaps



        