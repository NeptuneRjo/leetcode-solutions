from typing import List

class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     sorted_strs_list = sorted(strs, key=len, reverse=True)
        
    #     if len(sorted_strs_list[0]) == 0:
    #         return ""
    #     elif len(sorted_strs_list) == 1:
    #         return sorted_strs_list[0]
        
    #     base_string = sorted_strs_list[0]

    #     for index, string in enumerate(sorted_strs_list[1::]):
    #         updated_string = ""
    #         for char_index, char in enumerate(string):
    #             # prevent index errors
    #             if char_index > len(base_string) - 1:
    #                 break
                
    #             if char == base_string[char_index]:
    #                 updated_string += char
    #             else:
    #                 base_string = ""
    #         base_string = updated_string    

    #     return base_string

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        # set the default prefix to the first value in strs
        prefix = strs[0]
        # iterate through all but the first string
        for string in strs[1:]:
            # remove a letter from prefix untill only the matching letter(s) remain
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                
    
        return prefix
    