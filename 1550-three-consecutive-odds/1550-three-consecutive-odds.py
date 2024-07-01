class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 3
        for num in arr:
            counter = counter - 1 if num & 1 else 3
            if not counter:
                return  True
        return False

        # return "111" in "".join([str(num & 1) for num in arr])