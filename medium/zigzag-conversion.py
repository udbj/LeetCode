class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = []
        
        for i in range(numRows):
            rows.append([])
        
        lvert = -1
        strc = 0
        slen = len(s)
        
        
        if numRows > 1: 
        
            while strc < slen:
                while lvert < numRows:
                    lvert = lvert + 1
                    if lvert == numRows:
                        break
                    rows[lvert].append(s[strc])
                    print('Adding', s[strc], ' to row', lvert+1)


                    strc = strc + 1

                    if strc == slen:
                        break


                if strc == slen:
                    break

                lvert = lvert - 1

                while lvert > -1:
                    lvert = lvert - 1
                    if lvert == -1:
                        break

                    rows[lvert].append(s[strc])
                    print('Adding', s[strc], ' to row', lvert+1)

                    strc = strc + 1

                    if strc == slen:
                        break

                lvert = lvert + 1

            out = ''

            for row in rows:
                for char in row:
                    out = out + char
        else:
            out = s
                
        return out

# Alternative

class Alt_Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows > 1:
            irec = []
            rows = []

            for i in range(numRows):
                rows.append([])

            for i in range(numRows):
                irec.append(set())
            
            slen = len(s)
            k = 0
            pos = 2*numRows -3 + 1
            insc = 0

            while True:
                for i in range(numRows):
                    left = k*pos + i

                    if left >= slen:
                        continue

                    if left not in irec[i]:
                        rows[i].append(s[left])
                        insc = insc + 1
                        irec[i].add(left)

                    if insc == slen:
                        break

                    right = (k+1)*pos - i
                    if right >= slen:
                        continue

                    if right not in irec[i]:
                        rows[i].append(s[right])
                        insc = insc + 1
                        irec[i].add(right)

                    if insc == slen:
                        break


                if insc == slen:
                        break

                k = k + 1

            out = ''
            for row in rows:
                for char in row:
                    out = out + char

            return out
        
        else:
            return s
