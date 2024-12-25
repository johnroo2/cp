class TimeMap:

    def __init__(self):
        self.tm = {} #value, timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tm:
            val = self.tm[key]
            l, r = 0, len(val) - 1
            while l <= r:
                m = l + ((r - l) // 2)
                if val[m][1] == timestamp:
                    val[m][0] = value
                elif val[m][1] > timestamp:
                    r = m - 1
                else:
                    l = m + 1
            val.insert(l, (value, timestamp))
        else:
            self.tm[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.tm:
            val = self.tm[key]
            l, r = 0, len(val) - 1

            while l <= r:
                m = l + ((r - l) // 2)
                if val[m][1] == timestamp:
                    return val[m][0]
                elif val[m][1] > timestamp:
                    r = m - 1
                else:
                    l = m + 1

            while l >= 0:
                l -= 1
                if val[l][1] <= timestamp:
                    return val[l][0]
                    break
        return ""
            
        
