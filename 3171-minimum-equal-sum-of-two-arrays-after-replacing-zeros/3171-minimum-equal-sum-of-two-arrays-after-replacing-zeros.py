class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum_1, zeroes_1 = sum(nums1), nums1.count(0)
        sum_2, zeroes_2 = sum(nums2), nums2.count(0)
        if (zeroes_1 == 0 and sum_1 < sum_2 + zeroes_2 or
            zeroes_2 == 0 and sum_2 < sum_1 + zeroes_1
        ):
            return -1

        return max(sum_1 + zeroes_1, sum_2 + zeroes_2)