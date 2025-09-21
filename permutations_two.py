class Solution(object):
    def __iterate(self, current, step):
        if (step == self.size):
            self.ans.append(current[:])
            return
        last_added = None
        for idx in range(self.size):
           if (not self.taken[idx]) and (last_added != self.arr[idx]):
               self.taken[idx] = True
               current.append(self.arr[idx])
               self.__iterate(current, step + 1)
               last_added = current.pop()
               self.taken[idx] = False
    
    def permuteUnique(self, nums):
        self.arr = sorted(nums)
        self.size = len(nums)
        self.ans = []
        self.taken = [False for v in range(self.size)]
        self.__iterate([], 0)
        return self.ans