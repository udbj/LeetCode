class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDivide(size: int) -> bool:
            return sum((balls - 1) // size for balls in nums) <= maxOperations

        lo, hi = 1, 10 ** 9 + 1
        while lo < hi:
            size = lo + hi >> 1
            if canDivide(size):
                hi = size
            else:
                lo = size + 1
        return lo
