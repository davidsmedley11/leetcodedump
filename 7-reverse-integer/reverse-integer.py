class Solution:
    def reverse(self, x: int) -> int:
        print(-2 ** 31)
        x = str(x)
        x_reversed = (x)[::-1]
        x_reversed = x_reversed.replace("-", "")

        if int(x_reversed) > (2 ** 31) - 1:
            return 0
        elif "-" in x:
            return int(f"-{x_reversed}")
        else:
            return int(x_reversed)

        