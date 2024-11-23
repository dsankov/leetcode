class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box[0])
        for row in box:
            write_ptr = n - 1
            for read_ptr in range(n-1, -1, -1):
                if row[read_ptr] == "*":
                    write_ptr = read_ptr - 1
                elif row[read_ptr] == "#":
                    row[write_ptr], row[read_ptr] = row[read_ptr], row[write_ptr]
                    write_ptr -= 1

        box = zip(*(box[::-1]))
        return box
        