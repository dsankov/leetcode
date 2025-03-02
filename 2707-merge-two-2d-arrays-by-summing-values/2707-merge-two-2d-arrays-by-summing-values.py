class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        result = []
        idx1 = idx2 = 0
        while idx1 < n1 and idx2 < n2:
            id1, val1 = nums1[idx1]
            id2, val2 = nums2[idx2]
            if id1 < id2:
                result.append([id1, val1])
                idx1 += 1
            elif id2 < id1:
                result.append([id2, val2])
                idx2 += 1
            else:
                result.append([id1, val1 + val2])
                idx1 += 1
                idx2 += 1
        
        while  idx1 < n1 :
            result.append(nums1[idx1])
            idx1 += 1

        while  idx2 < n2:
            result.append(nums2[idx2])
            idx2 += 1

        return result

        