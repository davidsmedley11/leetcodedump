class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        index = 0
        s = s.lstrip()
        result = 0

        if not s:
            return 0
        
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        while index < len(s) and s[index].isdigit():
            result = (result * 10) + int(s[index])
            index += 1

        result = result * sign

        int_max = (2 ** 31) - 1
        int_min = - 2 ** 31

        if result > int_max:
            result = int_max
        elif result < int_min:
            result = int_min

        return result

