class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        new = 0

        while original > 0:
            """
            In order of operations:
            * Shift the new number to the left
            * Find the last digit of the original using modular operation
            * Add the shifted new number and the last digit
            * Remove the last digit from the original
            """
            new = new * 10 + original % 10
            original //= 10
        return new == x
    
a = Solution()
print(a.isPalindrome(120))