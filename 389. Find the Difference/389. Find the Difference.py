# using count method
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for x in t:
            if s.count(x) < t.count(x):
                return x

# using hash map


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dct = defaultdict(int)

        for x in s:
            dct[x] += 1
        for i in t:
            dct[i] -= 1
        for key, val in dct.items():
            if val != 0:
                return key
        return key
