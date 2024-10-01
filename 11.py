"""
11. Container With Most Water

"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        current_area = 0

        while left < right:
            new_area = min(height[left], height[right]) * (right - left)
            if new_area > current_area:
                current_area = new_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return current_area



if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    s.maxArea(height)

        