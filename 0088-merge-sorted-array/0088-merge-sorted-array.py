class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        read_1 = m - 1
        read_2 = n - 1
        write_1 = len(nums1) - 1
        while read_1 >= 0 and read_2 >= 0:
            if nums1[read_1] > nums2[read_2]:
                nums1[write_1] = nums1[read_1]
                read_1 -= 1
            else:
                nums1[write_1] = nums2[read_2]
                read_2 -= 1
            write_1 -= 1
        while read_1 >= 0:
            nums1[write_1] = nums1[read_1]
            read_1 -= 1
            write_1 -= 1
        while read_2 >= 0:
            nums1[write_1] = nums2[read_2]
            read_2 -= 1
            write_1 -= 1