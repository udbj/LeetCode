class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0
        for i,c in enumerate(s):
            w = set()
            w.add(c)
            c_len = 1
            
            for j,k in enumerate(s[i+1:]):
                if k not in w:
                    c_len = c_len + 1
                    w.add(k)
                else:
                    break
            if c_len > max_len:
                max_len = c_len
        
        return max_len
