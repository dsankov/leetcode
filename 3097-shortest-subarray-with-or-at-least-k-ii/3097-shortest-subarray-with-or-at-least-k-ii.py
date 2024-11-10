class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1

        MAX_BITS = ceil(log2(10**9)) + 1
        NEGATIVE_BIT = (2 ** MAX_BITS) - 1

        n = len(nums)
        left, right = 0, 0
        sliding_or = 0
        sliding_or_bits = [deque() for _ in range(MAX_BITS)]
        min_length = math.inf
        while left < n:
            if sliding_or < k:
                if right >= n:
                    break
                for bit_index in range(MAX_BITS):
                    if nums[right] & (1 << bit_index):
                        sliding_or_bits[bit_index].append(right)
                sliding_or |= nums[right]
                right += 1
            else:
                min_length = min(min_length, right - left)
                if min_length == 1:
                    return min_length
                for bit_index in range(MAX_BITS):
                    if nums[left] & (1 << bit_index):
                        sliding_or_bits[bit_index].popleft()
                        if len(sliding_or_bits[bit_index]) == 0:
                            sliding_or &= NEGATIVE_BIT ^ (1 << bit_index)
                left += 1

        return min_length if min_length != math.inf else -1