class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)
        num_idx = 0
        curr_group = 0

        num_to_group = {}
        num_to_group[sorted_nums[num_idx]] = curr_group

        group_to_list = defaultdict(deque)
        group_to_list[curr_group] = deque([sorted_nums[num_idx]])

        for num_idx, num in enumerate(sorted_nums[1:], start=1):
            if abs(sorted_nums[num_idx] - sorted_nums[num_idx-1]) > limit:
                curr_group += 1

            num_to_group[sorted_nums[num_idx]] = curr_group

            group_to_list[curr_group].append(sorted_nums[num_idx])

        for num_idx in range(len(nums)):
            num = nums[num_idx]
            group = num_to_group[num]
            nums[num_idx] = group_to_list[group].popleft()

        return nums