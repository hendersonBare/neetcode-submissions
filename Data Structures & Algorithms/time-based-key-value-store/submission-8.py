class TimeMap:

    def __init__(self):
        self.key_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_dict:
            self.key_dict[key]=[]
        self.key_dict[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_dict:
            return ""
        key_list = self.key_dict[key]
        l,r=0,len(key_list)-1

        while (l<=r):
            m = (l+r)//2
            if key_list[m][0]==timestamp:
                return key_list[m][1]
            elif key_list[m][0]<timestamp:
                l=m+1
            else:
                r=m-1
        if key_list[r][0]<timestamp:
            return key_list[r][1]
        return ""