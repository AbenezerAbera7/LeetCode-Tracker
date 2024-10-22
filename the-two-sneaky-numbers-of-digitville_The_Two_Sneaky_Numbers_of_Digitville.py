class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        counts = collections.Counter(nums)
        res = []
        for key, value in counts.items():
            if value == 2:
                res.append(key)
        return res
        