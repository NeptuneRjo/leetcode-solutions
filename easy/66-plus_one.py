from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # increase digits by one
        digit = int(''.join(map(str, digits)))
        digit += 1
        # split back into list
        # return the new list
        return [int(x) for x in str(digit)]