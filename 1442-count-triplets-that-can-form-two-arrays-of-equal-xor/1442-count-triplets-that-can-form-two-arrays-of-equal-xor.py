class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        
        start = 0
        xor_so_far = 0
        for start in range(n-1):
            xor_so_far = arr[start]
            for end in range(start+1, n):
                xor_so_far ^= arr[end]
                if xor_so_far == 0:
                    result += end - start
        
        return result
    
                    