from collections import Counter

class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.n1 = nums1
        self.n2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.freq[self.n2[index]] -= 1
        self.n2[index] += val
        self.freq[self.n2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for n in self.n1:
            if (tot-n) in self.freq:
                res += self.freq[tot-n]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)