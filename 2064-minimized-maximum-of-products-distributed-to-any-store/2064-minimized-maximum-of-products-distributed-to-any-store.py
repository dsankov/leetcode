class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        products_heap = [(-quantity, quantity, 1) for quantity in quantities]
        heapify(products_heap)
        for _ in range(n - m):
            (negative_quantity_per_store, 
                total_quantity,
                num_stores) = heappop(products_heap)
            heappush(products_heap,
                (
                - math.ceil(total_quantity / (num_stores + 1)),
                total_quantity,
                num_stores + 1
                ))

        return - heappop(products_heap)[0]