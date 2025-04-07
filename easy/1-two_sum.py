from typing import List

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     # return the 2 indices of nums thats values add up to target
    #     # assume there is exactly one solution, you may not use the same element twice
        
    #     # for each element in nums, add together each element in nums
    #     # if it's not the same element and it equals target, return
        
    #     # for each element
    #     for primary in range(len(nums)):
    #         # add each element
    #         for secondary in range(len(nums)):
    #             notSameElement = primary != secondary 
    #             equalsTarget = nums[primary] + nums[secondary] == target

    #             if notSameElement and equalsTarget:
    #                 return [primary, secondary]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # best case can be o(n)
        # for loop is o(n); if loop is o(1) 
        # o(n) is the slowest so it takes precedent

        storedNums = {}

        for index, value in enumerate(nums):
            # target = value + x
            # to find x we need to subtract the current value from the target value
            difference = target - value

            """
            we check if the difference between the target and the current value
            is already stored and return the index of the difference and current value
            """
            if difference in storedNums:
                return [storedNums[difference], index]

            """
            if they dont find the target, store it in the dictionary
            store the index of the current value
            """
            storedNums[value] = index
