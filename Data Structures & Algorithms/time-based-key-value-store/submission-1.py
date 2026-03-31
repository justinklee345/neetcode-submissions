class TimeMap:

    def __init__(self):
        self.storeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.storeMap.keys():
            self.storeMap[key].append((timestamp, value))
        else:
            self.storeMap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        print(key, timestamp)
        if key not in self.storeMap.keys():
            return ""

        lst = self.storeMap[key]
        l = 0
        r = len(lst) - 1
        current_best = -1
        while l <= r:
            m = l + ((r-l) // 2)
            
            if lst[m][0] == timestamp:
                return lst[m][1]
            elif lst[m][0] < timestamp:
                current_best = max(m, current_best)
                l = m + 1
            else:
                r = m - 1

        if (current_best) == -1:
            return ""
        return lst[current_best][1]

"""
(1, happy)

1 2 4 5 6 7 8 9
1 2 4
2 4 (0, 1)
"""



        
