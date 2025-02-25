class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even_arr_count = 1
        odd_arr_count = 0
        prefix_sum = 0
        total_odd_arr_count = 0
        for prefix_sum in itertools.accumulate(arr):
            if prefix_sum % 2 == 0:
                total_odd_arr_count += odd_arr_count
                odd_arr_count += 0
                even_arr_count += 1
            else:
                total_odd_arr_count += even_arr_count
                odd_arr_count += 1
                even_arr_count += 0

            total_odd_arr_count %= 10**9 + 7

        return total_odd_arr_count