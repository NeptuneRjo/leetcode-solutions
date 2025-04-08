class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_plus_b = int(a, 2) + int(b, 2)
        return bin(a_plus_b)[2:]