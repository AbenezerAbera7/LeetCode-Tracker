class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        DICT = collections.Counter(nums)

        for key, value in DICT.items():
            if value > 1:
                return True
        return False

        