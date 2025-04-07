from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # get the unique values from nums
        uniques = list(set(nums))
        # update nums so it contains the unique values in order
        nums[:len(uniques)] = sorted(uniques)
        # return the length of uniques (k)
        return len(uniques)


a = Solution()
print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))