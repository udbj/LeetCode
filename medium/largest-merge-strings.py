class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        a = list(word1)
        b = list(word2)
        c = []
        while len(a) >0 or len(b) > 0:
            if a > b:
                c.append(a[0])
                del a[0]
            else:
                c.append(b[0])
                del b[0]
        
        return ''.join(c)
