class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array_freq = {}
        for num in nums:
            array_freq[num] = array_freq.pop(num, 0) + 1
        # reverse it
        array_freq_rev = []
        for freq in array_freq.keys():
            array_freq_rev.append([array_freq[freq],freq])
        res = []
        sorted_arr = sorted(array_freq_rev, reverse=True)
        for i in range(len(sorted_arr)):
            if i == k:
                return res
            else:
                res.append(sorted_arr[i][1])
        return res