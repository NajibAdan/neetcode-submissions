class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums)+1)
        postfix = [1] * (len(nums)+1)
        res = []
        for i in range(len(nums)):
            # print(i,prefix,postfix)
            prefix[i+1] = prefix[i] * nums[i]
            postfix[len(nums)-i-1] = postfix[len(nums)-i] * nums[len(nums) - 1-i]
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[i+1])
        return res