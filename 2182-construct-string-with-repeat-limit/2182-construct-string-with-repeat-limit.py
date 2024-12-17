class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        chars_queue = [(-ord(char), count) for char, count in Counter(s).items()]
        heapify(chars_queue)
        result = []
        while chars_queue:
            neg_char, curr_count = heappop(chars_queue)
            curr_char = chr(-neg_char)
            if curr_count <= repeatLimit:
                result.extend([curr_char] * curr_count)
                continue
            result.extend([curr_char] * repeatLimit)
            if not chars_queue:
                break
            next_neg_char, next_count = heappop(chars_queue)
            next_char = chr(-next_neg_char)
            result.append(next_char)
            next_count -= 1
            if next_count > 0:
                heappush(chars_queue, (next_neg_char, next_count))
            heappush(chars_queue, (neg_char, curr_count-repeatLimit))


        return "".join(result)
        