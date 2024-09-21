class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current_number = 1

        for _ in range(n):
            result.append(current_number)

            if current_number * 10 <= n:
                current_number *= 10
            else:
                while (
                    current_number % 10 == 9
                    or current_number >= n
                ):
                    current_number //= 10
                current_number += 1

        return result
        