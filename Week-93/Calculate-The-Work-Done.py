class Solution:
    def workDone(self, n, cap, arr):
        # code here
        belt = []
        work = 0
        for item in arr:
            if item in belt:
                pass
            else:
                work += 1
                if len(belt) == cap:
                    belt.pop()
                belt.insert(0, item)
        return work
