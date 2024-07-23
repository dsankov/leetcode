class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        result = []
        freqs = sorted((frequency, -num) for (num, frequency) in Counter(nums).items())
        for frequency, num in freqs:
            result.extend([-num] * frequency)


        return result
        