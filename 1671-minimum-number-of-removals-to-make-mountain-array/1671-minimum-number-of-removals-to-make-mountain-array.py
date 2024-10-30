class Solution:
    def len_lis(self, nums: List[int]) -> List[int]:
        lis = [nums[0]]
        result = [0] * self.n
        for i in range(1, self.n):
            curr_num = nums[i]
            insert_index = bisect_left(lis, curr_num)
            if insert_index == len(lis):
                lis.append(curr_num)
            else:
                lis[insert_index] = curr_num
            result[i] = len(lis)
        return result    

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        self.n = len(nums)
        len_lis = self.len_lis(nums)
        len_lds = self.len_lis(nums[::-1])[::-1]
        result = math.inf
        for i in range(1, self.n - 1):
            if len_lis[i] != 1 and len_lds[i] != 1:
                result = min(result, self.n + 1 - len_lis[i] - len_lds[i])

        return result

        