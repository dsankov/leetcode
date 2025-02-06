class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pair_product_freqs = defaultdict(int)
        result = 0

        for first_idx, first_num in enumerate(nums):
            for second_idx, second_num in enumerate(nums[first_idx + 1:], start=first_idx + 1):
                product_value = first_num * second_num
                pair_product_freqs[product_value] += 1

        for product_freq in pair_product_freqs.values():
            pairs_of_equal_products = (product_freq - 1) * product_freq // 2
            result += 8 * pairs_of_equal_products

        return result
        