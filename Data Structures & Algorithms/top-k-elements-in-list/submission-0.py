class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] = (num, hashMap[num][1] + 1)
            else:
                hashMap[num] = (num, 1)
        hashMap = list(hashMap.values())
        hashMap.sort(reverse=True,key=lambda x: x[1])
        return [hashMap[x][0] for x in range(k)]