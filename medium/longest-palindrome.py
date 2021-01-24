class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        rs = s[::-1]
        ref = len(s)
        lmax = 0
        
        start = 0
        end = 0
        
        for i, c in enumerate(s):
            j = ref
            
            if lmax > ref-i-1:
                break
                
            while j > i-1:
                if s[j-1] == s[i]:
                    comp = set()
                    subs = s[i:j]
                    lsub = len(subs)
                    
                    comp.add(rs[ref-j:ref-i])
                    
                    if lsub > lmax and subs in comp:
                        start = i
                        end = j
                        lmax = lsub
                j = j -1

                
        return s[start:end]
        
                    
                
