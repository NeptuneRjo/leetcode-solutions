class Solution:
    def romanToInt(self, s: str) -> int:
        # s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        numerals_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        numerals = s
        total = 0
        
        while len(numerals) > 0:
            if numerals[:2] in numerals_dict:
                total += numerals_dict[numerals[:2]]
                numerals = numerals[2::]
            elif numerals[0] in numerals_dict:
                total += numerals_dict[numerals[0]]
                numerals = numerals[1::]
        return total

    
a = Solution()
print(a.romanToInt("MIX")) # 1009
print(a.romanToInt("CMLIV")) # 954