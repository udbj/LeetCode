class Solution:
    def countHomogenous(self, s: str) -> int:
        
        r = 1
        p = s[0]
        o = 0
        
        for c in s[1:]:
            if p == c:
                r += 1
            else:
                o += r*(r+1)/2
                r = 1
            p = c
        o += r*(r+1)/2
        
        return int(o % (10**9 + 7))
                
        
        
