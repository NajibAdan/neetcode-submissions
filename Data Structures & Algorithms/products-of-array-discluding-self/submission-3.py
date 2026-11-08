class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            res = 1
            for x in range(len(nums)):
                if x != i:
                    res = res * nums[x]
            i += 1
            ans.append(res)
        return ans