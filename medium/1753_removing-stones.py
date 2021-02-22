class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        nums = sorted([a,b,c])
        
        if nums[0] + nums[1] >= nums[2]:
            return sum(nums) >> 1
        else:
            return nums[0] + nums[1]
