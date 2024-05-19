class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        enumerated_costs = [(cost, i) for (i, cost) in enumerate(costs)]

        leading_ptr = candidates
        leading_heap = enumerated_costs[:leading_ptr]
        heapify(leading_heap)

        trailing_ptr = max(leading_ptr, n - candidates)
        trailing_heap = enumerated_costs[trailing_ptr:]
        heapify(trailing_heap)

        total_sum = 0
        while k > 0:
            if leading_heap:
                leading_min, leading_index = leading_heap[0]
            else:
                leading_min, leading_index = math.inf, -1
                
            if trailing_heap:     
                trailing_min, trailing_index = trailing_heap[0]
            else:
                trailing_min, trailing_index = math.inf, -1

            if leading_min <= trailing_min:
                total_sum += leading_min
                heappop(leading_heap)

                if leading_ptr  < trailing_ptr:
                    heappush(leading_heap, enumerated_costs[leading_ptr])
                    leading_ptr += 1
                if leading_index == trailing_index:
                    heappop(trailing_heap)

            else:
                total_sum += trailing_min
                heappop(trailing_heap)

                if trailing_ptr > leading_ptr:
                    trailing_ptr -= 1
                    heappush(trailing_heap, enumerated_costs[trailing_ptr])

            k -= 1

        return total_sum