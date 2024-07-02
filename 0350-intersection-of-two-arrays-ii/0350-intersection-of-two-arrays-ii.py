class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        i, j = 0, 0
        result = []
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
        