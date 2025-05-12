class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digit_counts = Counter(digits)
        result = []
        for cur_num in range(100, 1000, 2):
            cur_num_digits = Counter(str(cur_num))
            while cur_num_digits:
                cur_digit, cur_count = cur_num_digits.popitem()
                if cur_count > digit_counts[int(cur_digit)]:
                    break
            else:
                result.append(cur_num)

        return result

        