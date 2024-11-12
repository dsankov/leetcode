class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        items.sort()
        indexed_queries = [(query, i) for i, query in enumerate(queries)]
        indexed_queries.sort()

        result = [0] * len(queries)
        max_beauty = 0
        item_index = 0
        for query, original_index in indexed_queries:
            while item_index < n and query >= items[item_index][0]:
                max_beauty = max(max_beauty, items[item_index][1])
                item_index += 1
            result[original_index] = max_beauty
        return result


        