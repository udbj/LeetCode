class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        for (a,b) in edges:
            g[a].add(b)
            g[b].add(a)
            
        d = collections.defaultdict(int)
        for n in g:
            d[n] = len(g[n])
            
        res = float('inf')
        for n in g:
            for m in g[n]:
                for o in g[n] & g[m]:
                    res = min(res, d[n]+d[m]+d[o]-6)
                    if n in g[o]:
                        g[o].remove(n)
                if n in g[m]:
                    g[m].remove(n)
        if res == float('inf'):
            return -1
        else:
            return res
