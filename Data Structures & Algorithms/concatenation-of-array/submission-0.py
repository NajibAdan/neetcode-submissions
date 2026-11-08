class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        i = 0
        while i < len(nums): 
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]
            i += 1
        return ans