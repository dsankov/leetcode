class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_nums = set()
        result = []
        for i, (a_num, b_num) in enumerate(zip(A, B)):
            seen_nums.add(a_num)
            seen_nums.add(b_num)
            result.append(2 * (i+1) - len(seen_nums))
        return result
        