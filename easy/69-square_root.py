class Solution:
    def mySqrt(self, x: int) -> int:
        # use repeated subtraction
        index = 0
        total = x
        subtract = 1

        while total > 0:
            index += 1
            total -= subtract
            subtract += 2

        if total < 0:
            index -= 1

        return index

a = Solution()
print(a.mySqrt(17))