"""
LeetCode 9: Palindrome Number (Easy)

Problem Summary:
Given an integer, determine whether it is a palindrome.
A palindrome reads the same forward and backward.

Approach:
- Convert the integer to a string.
- Reverse the string.
- Compare the reversed string with the original.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        values = str(x)
        reversed_value = values[::-1]
        if reversed_value == values:
            return True
        else:
            return False