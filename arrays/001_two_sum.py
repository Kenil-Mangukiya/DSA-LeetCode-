"""
LeetCode 1: Two Sum (Easy)

Problem Summary:
Given an array of integers and a target value, find the indices of two
different numbers such that their sum equals the target.

Approach:
- Use a brute-force nested loop.
- Check every possible pair until the correct sum is found.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

