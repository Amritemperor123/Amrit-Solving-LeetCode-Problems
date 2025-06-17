from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
def main():
    input_string = str(input("Enter the array: "))
    input_string = input_string.strip('[]') 
    nums = list(map(int, input_string.split(',')))

    val = int(input("Enter target:"))

    solution = Solution()
    k = solution.removeElement(nums, val)
    print(f"Output: {k}, nums = {nums[:k]}")

if __name__ == "__main__":
    main()