from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if sum == 0:
                        triplet = [nums[i], nums[left], nums[right]]
                        triplets.append(triplet)
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sum < 0:
                        left += 1
                    else:
                        right -= 1
        return triplets
                    

def main():
    input_string = str(input("Enter the array: "))
    input_string = input_string.strip('[]') 
    nums = list(map(int, input_string.split(',')))

    Solution = Solution(nums)