from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area_final = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > area_final:
                area_final = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1  
        return area_final        

def main():
    input_string = str(input("Enter the array: "))
    input_string = input_string.strip('[]') 
    height = list(map(int, input_string.split(',')))

    solution = Solution(height)