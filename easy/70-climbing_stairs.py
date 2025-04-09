class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        base = 0

        if n <= 2:
            return n

        for i in range(n):
            base = first + second
            first = second
            second = base
        
        return base

    
a = Solution()
print(a.climbStairs(4))