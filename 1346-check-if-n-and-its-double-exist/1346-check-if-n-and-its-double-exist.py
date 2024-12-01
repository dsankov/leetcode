class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen_numbers = set()
        for num in arr:
            if num * 2 in seen_numbers:
                return True
            if num % 2 == 0:
                if num // 2 in seen_numbers:
                    return True
            seen_numbers.add(num)
        return False