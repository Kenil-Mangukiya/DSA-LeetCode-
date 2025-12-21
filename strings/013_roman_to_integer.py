"""
LeetCode 13: Roman to Integer (Easy)

Problem Summary:
Given a Roman numeral string, convert it into its integer value.
Roman numerals use specific symbols with fixed values and follow
addition and subtraction rules based on symbol order.

Approach:
- Map Roman symbols to their integer values.
- Traverse the string from left to right.
- Compare the current symbol with the next one:
  - If current value is smaller than the next, subtract it.
  - Otherwise, add it.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        integer_value = 0
        values = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        integer_value = 0
        
        for i in range(len(s)):
            current_value = values[s[i]]

            if i + 1 < len(s) and current_value < values[s[i+1]]:
                integer_value -= current_value
            else:
                integer_value += current_value

        return integer_value
            



        