class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        if n == 1:
            return [True] * len(queries)

        special_edges = []    
        for i in range(0, n-1):
            curr_num = nums[i]
            next_num = nums[i+1]
            if curr_num % 2 == next_num % 2:
                special_edges.append(i)
        special_edges.append(n-1)

        result = []
        for q_start, q_end in queries:
            if bisect_left(special_edges, q_start) == bisect_left(special_edges, q_end):
                result.append(True)
            else:
                result.append(False)
        return result



        