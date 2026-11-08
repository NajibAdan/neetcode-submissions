class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_pos = -1
        zero_count = 0
        for i,num in enumerate(nums):
            if num!= 0:
                total_product *= num
            else:
                zero_pos = i
                zero_count += 1
        if zero_count > 1:
            return [0] * len(nums)
        if zero_pos > -1:
            results = [0] * len(nums)
            results[zero_pos] = total_product
            return results
        results = [total_product] * len(nums)
        for i, num in enumerate(nums):
            results[i] = int(results[i] / num)
        return results