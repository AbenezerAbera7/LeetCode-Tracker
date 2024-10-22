class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = collections.Counter(nums)
        n = len(nums)

        res = []

        for key, value in count.items():
            if value > (n/3):
                res.append(key)
        return res
        