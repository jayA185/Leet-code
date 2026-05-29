class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()   # remove leading spaces

        if not s:
            return 0

        sign = 1
        index = 0
        result = 0

        # check sign
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1

        # convert digits
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        result *= sign

        # 32-bit integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result