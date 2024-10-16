class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        letters_counter = [(-count, letter) for count, letter in zip([a, b, c], ["a", "b", "c"]) if count > 0]
        heapify(letters_counter)

        while letters_counter:
            count, letter = heappop(letters_counter)
            count = -count
            if len(result) >= 2 \
                and result[-1] == letter and result[-2] == letter:
                    if letters_counter:
                        next_count, next_letter = heappop(letters_counter)
                        next_count = -next_count
                        result.append(next_letter)
                        next_count -= 1
                        if next_count > 0:
                            heappush(letters_counter, (-next_count, next_letter))
                    else:
                        break
            result.append(letter)
            count -= 1
            if count > 0:
                heappush(letters_counter, (-count, letter))
        return "".join(result)

        