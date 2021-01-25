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
