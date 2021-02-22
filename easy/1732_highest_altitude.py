class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        c = 0
        for n in gain:
            c += n
            if c > m:
                m = c
        
        return m
