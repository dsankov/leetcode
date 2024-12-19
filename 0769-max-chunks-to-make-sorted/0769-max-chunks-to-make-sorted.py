class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for idx, num in enumerate(arr):
            if not stack or stack[-1] < num:
                stack.append(num)
                continue
            
            max_so_far = stack[-1]
            while stack and stack[-1] > num:
                stack.pop()
            stack.append(max_so_far)

        return len(stack)