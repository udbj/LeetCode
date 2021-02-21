class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        l = 0
        m = 0
        s = 0
        
        
        if a >= b and a >= c:
            l = a
            if b >= c:
                m = b
                s = c
            else:
                m = c
                s = b
        
        elif b >= c and b >= a:
            l = b
            if a >= c:
                m = a
                s = c
            else:
                m = c
                s = a
        
        elif c >= a and c >= b:
            l = c
            if a >= b:
                m = a
                s = b
            else:
                m = b
                s = a

        if m + s >= l:
            return (m + s + l) >> 1
        else:
            return m + s
        
        
        
