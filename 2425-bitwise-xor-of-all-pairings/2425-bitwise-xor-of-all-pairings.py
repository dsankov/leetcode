class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        return reduce(xor, len(nums1) % 2 * nums2 + len(nums2) % 2 * nums1, 0)

        