class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        
        X = set()
        l = len(nums) >> 1
        h1 = nums[:l]
        k = 1
        while k <= len(h1):
            for c in itertools.combinations(h1, k):
                X.add(sum(c))
            k += 1
        X.add(0)
        Y = set()
        
        h2 = nums[l:]
        k = 1
        while k <= len(h2):
            for c in itertools.combinations(h2, k):
                Y.add(sum(c))
            k += 1
        
        Y.add(0)
        
        m = abs(goal)
        Y = sorted(Y)
        
        for x in X:
            remain = goal- x
            i=bisect_left(Y,remain)
            
            if i<len(Y):
                m = min(m,abs(remain - Y[i]))
                
            if i>0:
                m = min(m,abs(remain - Y[i-1]))
        
        return m
