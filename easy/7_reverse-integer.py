class Solution:
    def reverse(self, x: int) -> int:
        
        rmax = 2**31 - 1
        rmin = -2**31
        
        n = False
        if x < 0:
            x = -x
            n = True
        
        y = 0
        while x > 0:
            y = y*10 + x % 10
            x = x//10
        
        if n:
            y = -y
        
        if y < rmin or y > rmax:
            y = 0
        
        return y
