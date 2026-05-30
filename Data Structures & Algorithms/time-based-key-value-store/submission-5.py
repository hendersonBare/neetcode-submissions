class TimeMap:

    def __init__(self):
        self._map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self._map:
            self._map[key].append([value, timestamp]) #using arr instead of tuple since tuples are immutable
        else:
            self._map[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._map:
            return ""
        else:
            arr = self._map[key]
            print(arr)
            l, r = 0, len(arr)-1
            while l < r:
                mid = (l+r)//2
                if arr[mid][1] == timestamp:
                    return arr[mid][0]
                elif arr[mid][1] < timestamp:
                    l = mid+1
                else:
                    r = mid-1
            print(l,r)
            mid = (l+r)//2
            if arr[mid][1] <= timestamp:
                return arr[mid][0]
            elif mid-1 >= 0 and arr[mid-1][1] <= timestamp:
                return arr[mid-1][0]
            return ""
            
