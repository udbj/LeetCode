class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        rs = s[::-1]
        ref = len(s)
        lmax = 0
        
        start = 0
        end = 0
        
        for i, c in enumerate(s):
            j = ref
            end_points  = set()
            if lmax > ref-i:
                break
            while j > i-1:
                if s[j-1] == s[i]:
                    end_points.add(j)
                j = j -1
            
            for pt in end_points:
                comp = set()
                subs = s[i:pt]
                lsub = len(subs)
                
                comp.add(rs[ref-pt:ref-i])
                
                if lsub > lmax and subs in comp:
                    start = i
                    end = pt
                    lmax = lsub

                
        return s[start:end]
        
                    
                
