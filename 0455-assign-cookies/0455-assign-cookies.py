class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapify(g)
        heapify(s)
        result = 0
        while g:
            child = heappop(g)
            while s:
                cookie = heappop(s)
                if child <= cookie:
                    result += 1
                    break
        return result