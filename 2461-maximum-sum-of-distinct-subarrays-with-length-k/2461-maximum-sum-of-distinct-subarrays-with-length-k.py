class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_freqs = Counter(nums[:k])
        num_of_nondistinct_nums = sum(freq > 1 for freq in subarray_freqs.values())
        curr_subarray_sum = sum(nums[:k])
        max_subarray_sum =  curr_subarray_sum if num_of_nondistinct_nums == 0 else 0
        for i in range(k, n):
            curr_subarray_sum += nums[i] - nums[i-k]
            
            if subarray_freqs[nums[i-k]] == 2:
                num_of_nondistinct_nums -= 1
            subarray_freqs[nums[i-k]] -= 1
            if subarray_freqs[nums[i]] == 1:
                num_of_nondistinct_nums += 1
            subarray_freqs[nums[i]] += 1

            if num_of_nondistinct_nums == 0:
                max_subarray_sum = max(max_subarray_sum, curr_subarray_sum)
        return max_subarray_sum