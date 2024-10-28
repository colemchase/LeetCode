class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 1
        for num in nums:
            temp = 1
            while num**2 in nums:
                temp+=1
                num**=2
            res = max(temp, res)
        return res if res != 1 else -1
