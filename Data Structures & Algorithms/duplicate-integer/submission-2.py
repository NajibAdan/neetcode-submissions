class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkedset = set()
        for num in nums:
            if num in checkedset:
                return True
            else:
                checkedset.add(num)

        return False