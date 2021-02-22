class Solution:
          
    def maximumTime(self, time: str) -> str:
        
        out = ''
        if time[0] == '?' or time[1] == '?':
            if time[0] == '?' and time[1] == '?':
                out = out + '23'
            elif time[0] == '?':
                itm = int(time[1])
                if itm > 3:
                    out = out + '1'
                else:
                    out = out + '2'
                out = out + time[1]

            elif time[1] == '?':
                out = out + time[0]
                if time[0] == '2':
                    out = out + '3'
                else:
                    out = out + '9'
        else:
            out = out + time[0] + time[1]
        out = out + ':'
        
        if time[3] == '?':
            out = out + '5'
        else:
            out = out + time[3]
        if time [4] == '?':
            out = out + '9'
        else:
            out = out + time[4]
        
        return out
