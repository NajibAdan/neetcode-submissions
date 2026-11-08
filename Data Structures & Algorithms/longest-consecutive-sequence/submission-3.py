class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        scale = abs(max(nums)) + abs(min(nums) )
        min_1 = min(nums)
        idx = [False] * (scale + 1)
        for i in nums:
            # print(idx,i)
            idx[i-min_1] = True
        i = 0
        seq = 0
        longest = 0
        print(sorted(nums), idx)
        while i < len(idx):
            if idx[i] == True:
                seq += 1
            elif idx[i] == False:
                longest = max(longest,seq)
                seq = 0
            i += 1
        longest = max(longest,seq)
        return longest
