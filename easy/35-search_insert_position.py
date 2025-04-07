from typing import List


class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     # return the index of target in the list nums
    #     # if target is not in nums, return its index if it were inserted in order

    #     try:
    #         return nums.index(target)
    #     except ValueError:
    #         nums.insert(target, 0) # O(n)
    #         sorted_nums = sorted(nums) # O(n log n)
    #         return sorted_nums.index(target) # O(1)

    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # iterate through nums
        # while num is less than target, continue
        # if num equal target, return index
        # if num greater than, return index

        for index, num in enumerate(nums): # O(n)
            if num < target and index == len(nums) - 1: # O(1)
                return len(nums) # O(1)
            elif num == target or num > target:
                return index