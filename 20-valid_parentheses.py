class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { '(':')', '{':'}', '[':']' }
        stack = []

        for index, char in enumerate(s):
            if char in brackets:
                stack.insert(0, char)
            elif len(stack) > 0 and char == brackets[stack[0]]:
                stack.pop(0) 
            else: return False

        return len(stack) == 0
    
a = Solution()
print(a.isValid(']'))
print(a.isValid("([([)]])"))