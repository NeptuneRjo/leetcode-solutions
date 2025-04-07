from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove all instances of val from nums
        cleansed_nums = [i for i in nums if i != val]
        # update nums to the new list
        nums[:len(cleansed_nums)] = cleansed_nums
        # return the number of elements that are not equal to val
        return len(cleansed_nums)