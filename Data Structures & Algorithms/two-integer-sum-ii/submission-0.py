class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(numbers)):
            if numbers[i] in hashMap:
                return [hashMap[numbers[i]], i+1]
            else:
                hashMap[target-numbers[i]] = i+1