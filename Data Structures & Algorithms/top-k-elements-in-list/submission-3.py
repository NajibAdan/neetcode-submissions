class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        
        for num in nums:
            freq_dict[num] = freq_dict.pop(num, 0) + 1
        array_freq = [[] for i in range(len(nums) + 1)]
        for num, freq in freq_dict.items():
            array_freq[freq].append(num)
        result = []
        for i in range(len(array_freq)-1,-1, -1):
            for num in array_freq[i]:
                result.append(num)
                if len(result) >= k:
                    return result
    