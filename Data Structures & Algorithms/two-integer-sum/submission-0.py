class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for x in range(len(nums)):
            if nums[x] in hashmap: 
                return [hashmap[nums[x]] , x]
            else:
                b = target - nums[x]
                hashmap[b] = x