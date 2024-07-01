class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # counter = 0
        # for num in arr:
        #     counter = 0 if num % 2 == 0 else counter + 1
        #     if counter == 3:
        #         return  True
        # return False

        return "111" in "".join([str(num & 1) for num in arr])