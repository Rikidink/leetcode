"""
1. Two Sum
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}
        for i, v in enumerate(nums):
            r = target - v
            if r in h:
                return [i,h[r]]
            h[nums[i]] = i