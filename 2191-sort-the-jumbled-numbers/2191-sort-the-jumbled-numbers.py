class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        jumbled_nums = []
        for i, num in enumerate(nums):
            jumbled_num = int("".join([str(mapping[int(digit)]) for digit in str(num)])) 
            jumbled_nums.append((jumbled_num, i))
        answer = []   
        for _, i in sorted(jumbled_nums):
            answer.append(nums[i])
        return answer 
        