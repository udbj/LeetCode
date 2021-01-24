class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        posn = {}
        
        for c in range(10):
            posn[str(c)] = []
        for c in string.ascii_lowercase:
            posn[c] = []
        
        for c in string.ascii_uppercase:
            posn[c] = []
        
        for i,c in enumerate(s):
            posn[c].append(i)
            
        rs = s[::-1]
        ref = len(s)
        lmax = 0
        
        start = 0
        end = 0
        
        for i, c in enumerate(s):
            j = ref
            if lmax > max(posn[c])-i+1:
                continue
            
            for j in posn[c]:
                if j > i-1:
                    comp = set()
                    subs = s[i:j+1]
                    lsub = len(subs)
                    
                    comp.add(rs[ref-j-1:ref-i])
                    if lsub > lmax and subs in comp:
                        start = i
                        end = j + 1
                        lmax = lsub
                j = j -1

                
        return s[start:end]
        
                    
                
