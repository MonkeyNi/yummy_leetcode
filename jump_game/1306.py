class Solution:
    def canReach(self, arr, start):
        if start >=0 and start < len(arr) and arr[start] >= 0:
            # record checked number
            arr[start] = -arr[start]
            return arr[start] == 0 or self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])
        return False