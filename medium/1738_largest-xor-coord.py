class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        m = len(matrix[0])
        
        mem = [0]*m
        
        vals = list()
        
        for i in range(n):
            rtl = 0
            for j in range(m):
                rtl = rtl ^ matrix[i][j]
                mem[j] = mem[j] ^ rtl
                vals.append(mem[j])
        
        return sorted(vals, reverse = True)[k-1]
