from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # the last non-zero in nums1
        p1 = m - 1
        # the end of nums2
        p2 = n - 1
        # the end of nums1
        p3 = m + n - 1

        # while we can still iterate through nums2
        while p2 >= 0:
            # if we havent iterated through all of nums1, and nums1[p1] is greater than nums2[p2], set nums[p3] to nums1[p1]
            if p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1 
        print(nums1)

a = Solution()
# a.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
# a.merge([2,0], 1, [1], 1)
a.merge([4,5,6,0,0,0], 3, [1,2,3], 3)
# a.merge([0,0,0,0,0], 0, [1,2,3,4,5], 5)