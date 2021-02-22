class Solution:
    def minimumBoxes(self, n: int) -> int:
        
        m = 0
        totl = 0
        while True:
            totl = (m+1)*(m+2)*(m+3)/6
            if totl > n:
                break
            m += 1
        
        totl = m*(m+1)*(m+2)/6
        base = m * (m+1)/2
        rem = n - totl
        
        gap = 0
        while rem > 0:
            rem -= 1
            base +=1
            rem -= gap
            gap += 1

        return int(base)
