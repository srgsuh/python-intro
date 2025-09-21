class Solution(object):
    def __encode(self, arr):
        encoded = []
        count = 1
        value = ""
        isFirst = True
        for v in arr:
            if isFirst:
                isFirst = False
                value = v
                continue
            elif v == value:
                count += 1
                continue
            else:
                encoded.append(str(count))
                encoded.append(value)
                value = v
                count = 1
        encoded.append(str(count))
        encoded.append(value)
        return encoded
    
    def countAndSay(self, n):
        curr = ["1"]
        step = 1
        while step < n:
            step += 1
            curr = self.__encode(curr)
        return "".join(curr)