class Solution:
    def minOperations(self, s: str) -> int:
        
        
        nums = ['1','0']
        
        
        
        # start with 0
        p = s[0]
        if p == '0':
            o1 = 0
        else:
            o1 = 1
        p = '0'
        for c in s[1:]:
            if c == p:
                p = nums[int(c)]
                o1 += 1
            else:
                p = c
        
        # start with 1
        p = s[0]
        if p == '1':
            o2 = 0
        else:
            o2 = 1
        p = '1'
        for c in s[1:]:
            if c == p:
                p = nums[int(c)]
                o2 += 1
            else:
                p = c
        
        return min(o1,o2)
