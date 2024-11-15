class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        end_of_start_sorted_part = 0
        i = end_of_start_sorted_part + 1
        while i < n:
            if arr[i-1] <= arr[i]:
                end_of_start_sorted_part = i
                i += 1
            else:
                break
        start_of_end_sorted_part = n - 1
        i = start_of_end_sorted_part - 1
        while i >= 0:
            if arr[i] <= arr[i+1]:
                start_of_end_sorted_part = i
                i -= 1
            else:
                break

        min_length_of_mid_part = min(n - 1 - end_of_start_sorted_part, start_of_end_sorted_part)
        if min_length_of_mid_part == 0:
            return 0
        left = 0
        right = start_of_end_sorted_part
        while left <= end_of_start_sorted_part and right < n:
            while right < n and arr[left] > arr[right]:
                right += 1                
            min_length_of_mid_part = min(min_length_of_mid_part,
                                         right - 1 - left)
            left += 1

        return min_length_of_mid_part        