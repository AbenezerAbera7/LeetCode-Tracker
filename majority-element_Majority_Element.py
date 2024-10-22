class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dictu = collections.Counter(nums)
        n = len(nums)

        for key, value in dictu.items():
            if value > n / 2:
                return key