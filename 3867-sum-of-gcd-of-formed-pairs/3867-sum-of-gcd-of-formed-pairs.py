class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        mx = -inf
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(math.gcd(mx, num))
        prefixGcd.sort()
        result = 0
        for i in range(n // 2):
            a, b = prefixGcd[i], prefixGcd[n-1 - i]
            result += math.gcd(a, b)


        return result