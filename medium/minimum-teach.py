class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        n_users = set()
        c = Counter()
        n = 0
        
        for f in friendships:
            u1 = f[0] - 1
            u2 = f[1] - 1
            if u1 not in n_users or u2 not in n_users:
                if len(set(languages[u1]).intersection(set(languages[u2]))) == 0:
                    if u1 not in n_users:
                        n_users.add(u1)
                        c.update(languages[u1])
                        n+=1
                    if u2 not in n_users:
                        n_users.add(u2)
                        c.update(languages[u2])
                        n+=1
                

        if len(n_users) == 0:
            return 0
        else:
            k,v = c.most_common(1)[0]

            return n-v
        
