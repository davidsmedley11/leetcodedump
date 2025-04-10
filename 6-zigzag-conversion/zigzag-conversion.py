class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        rows = [""] * numRows
        current_row = 1
        going_down = False

        if numRows == 1 or numRows >= len(s):
            return s

        for char in s:
            rows[current_row - 1] += char
            if current_row == 1 or current_row == numRows:
                going_down = not going_down
            if going_down:
                current_row += 1
            elif not going_down:
                current_row -= 1
        
        zigzag = ''.join(rows)

        return zigzag

