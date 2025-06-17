from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        print("No integers available as solution!")
        return []

def main():
    input_string = str(input("Enter integers to the array: "))
    input_string = input_string.strip('[]') 
    nums = list(map(int, input_string.split(',')))
    target = int(input("Enter target integer: "))

    if len(nums) < 2:
        print("The array cannot contain such a small number of elements!")
        entry = int(input("Enter another element: "))
        nums.append(entry)

    solution = Solution()
    indices = solution.twoSum(nums, target)
    if indices:
        print(f"The indices are: {indices}")

if __name__ == "__main__":
    main()
