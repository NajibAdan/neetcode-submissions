class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        return [[x[0],x[1],x[2]] for x in res]