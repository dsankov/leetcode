class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cumulative_flip = 0
        flip_queue = deque([0] * k)
        result = 0
        for i in range(n):
            cumulative_flip ^= flip_queue.popleft()
            if cumulative_flip != nums[i]:
                flip_queue.append(0)
            else:
                if i > n - k:
                    return -1
                cumulative_flip ^= 1
                flip_queue.append(1)
                result += 1
            
        return result
        
