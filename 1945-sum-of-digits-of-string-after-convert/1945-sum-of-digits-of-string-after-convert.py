class Solution:
    def getLucky(self, s: str, k: int) -> int:
        char_to_int = {}
        for char in string.ascii_lowercase:
            char_to_int[char] = (1 + ord(char) - ord("a")) // 10 + (1 + ord(char) - ord("a")) % 10
        str_sum = 0
        for char in s:
            str_sum += char_to_int[char]
        for i in range(1, k):
            if str_sum < 10:
                return str_sum
            update_sum = 0
            while str_sum > 0:
                update_sum += str_sum % 10
                str_sum //= 10
            str_sum = update_sum
        return str_sum