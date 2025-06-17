from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
    
def main():
    input_string = str(input("Enter the array: "))
    input_string = input_string.strip('[]') 
    nums = list(map(int, input_string.split(',')))

    solution = Solution()
    k = solution.removeDuplicates(nums)
    print(f"Output: {k}, nums = {nums[:k] + ['_'] * (len(nums) - k)}")

if __name__ == "__main__":
    main()