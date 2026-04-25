import bisect


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:

        def flatten(p):
            x, y = p
            if y == 0:
                return x
            if x == side:
                return side + y
            if y == side:
                return 3 * side - x
            return 4 * side - y

        arr = sorted(flatten(p) for p in points)
        n = len(arr)

        def Valid(d):
            for i in range(n):
                ptr = i
                start_p = arr[i]
                cnt = 1

                while cnt < k:
                    target = arr[ptr] + d
                    j = bisect.bisect_left(arr, target)

                    if j == n:
                        break
                    if (start_p + 4 * side) - arr[j] < d:
                        break

                    ptr = j
                    cnt += 1

                else: # no break occured <=> cnt == k
                    return True

            return False

        low, high = 0, side
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if Valid(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
