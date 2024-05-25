class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        read = 0
        number = nums[read]
        
        read += 1
        write = read

        while read < n:
            if nums[read] == number:
                read += 1
            else:
                number = nums[read]                
                nums[write] = number
                write += 1
                read += 1        
        return write

