class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if num in difference.keys():
                return [difference[num], i]
            else:
                difference[diff] = i
            print(num, diff, difference)
        