class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        
        hFences = sorted(chain(hFences,[1, m]))
        h_deltas = set()
        for idx_top, top in enumerate(hFences):
            for bottom in hFences[-1: idx_top: -1]:
                h_deltas.add(bottom - top)

        vFences = sorted(chain(vFences, [1, n]))
        max_common_delta = 0
        for idx_left, left in enumerate(vFences):
            for right in vFences[-1: idx_left: -1]:
                if right - left in h_deltas:
                    max_common_delta = max(max_common_delta, right - left)
                    break

        return pow(max_common_delta, 2, 10**9 + 7) or -1
