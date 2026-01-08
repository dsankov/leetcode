class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}

        def buid_product_matrix(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return -math.inf
            if (i, j) in memo:
                return memo[(i,j)]
            memo[(i, j)] = max(
                nums1[i] * nums2[j],
                nums1[i] * nums2[j] + buid_product_matrix(i+1, j+1),
                buid_product_matrix(i+1, j),
                buid_product_matrix(i, j+1)
                )

            return memo[(i,j)]

        buid_product_matrix(0, 0)
        # print(memo)
        return memo[(0,0)]