class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box[0])
        for row in box:
            write_ptr = n
            while write_ptr >= 0:
                write_ptr -= 1
                while write_ptr >= 0 and row[write_ptr] != ".":
                    write_ptr -= 1
                read_ptr = write_ptr - 1
                while read_ptr >= 0:
                    if row[read_ptr] == "*":
                        write_ptr = read_ptr 
                        break
                    if row[read_ptr] == "#":
                        row[write_ptr] = "#"
                        write_ptr -= 1
                        row[read_ptr] = "."

                    read_ptr -= 1

        box = zip(*(box[::-1]))
        return box
        