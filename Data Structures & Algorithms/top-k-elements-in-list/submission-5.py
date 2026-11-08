class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_freq = {}
        for num in nums:
            count_freq[num] = count_freq.get(num,0) + 1
        freq_arr = [[] for i in range(len(nums)+1)]
        for freq, cnt in count_freq.items():
            freq_arr[cnt].append(freq)
        res_arr = []
        for i in range(len(freq_arr)-1, 0, -1):
            for num in freq_arr[i]:
                res_arr.append(num)
                if len(res_arr) == k:
                    return res_arr