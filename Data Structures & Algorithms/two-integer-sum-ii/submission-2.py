class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = j = 0
        while i < len(numbers):
            num = numbers[i]
            diff = target - num
            while j < len(numbers) and numbers[j] <= diff:
                if numbers[j] == diff:
                    return [i+1, j+1]
                else:
                    j += 1
            i += 1
            j = 1