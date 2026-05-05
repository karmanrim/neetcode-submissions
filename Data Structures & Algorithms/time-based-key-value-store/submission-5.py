class TimeMap:

    def __init__(self):
        self.vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.vals.get(key) is None:
            self.vals[key] = [[value], [timestamp]]
        else:
            self.vals[key][0].append(value)
            self.vals[key][1].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        v_t = self.vals.get(key, [])
        if v_t != []:
            values, timestamps = v_t
        else:
            values, timestamps = [''], []
        l, r = 0, len(timestamps)
        while r - l > 1:
            m = (r + l) // 2
            if timestamps[m] <= timestamp:
                l = m
            else:
                r = m
        if l == 0 and len(timestamps) > 0 and timestamp < timestamps[0]:
            return ''
            
        return values[l]
