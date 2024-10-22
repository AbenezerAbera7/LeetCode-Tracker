class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        maxu = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] <= nums[j]:
                    maxu = max(maxu, j - i)
        return maxu
        