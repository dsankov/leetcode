class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        max_dist = 0
        i, j = 0, -1
        while i < n:
            j = max(i - 1, j)
            while (j + 1) < m:
                if nums1[i] <= nums2[j + 1]:
                    j += 1
                else:
                    break
            # else:
            #      if nums1[i] <= nums2[j]:
            max_dist = max(max_dist, j - i)
            print(i, j)
            i += 1
        return max_dist