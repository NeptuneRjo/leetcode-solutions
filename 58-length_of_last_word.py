class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split s by whitespace
        s_list = s.split()
        # return the length of the last element
        return len(s_list[-1])