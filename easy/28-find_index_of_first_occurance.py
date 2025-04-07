class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return the index of the first occurance of needle in haystack
        # if needle is not present, return -1
        return haystack.find(needle)