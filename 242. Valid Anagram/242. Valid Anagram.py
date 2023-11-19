# using sort

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# using hash table


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct = defaultdict(int)

        for x in s:
            dct[x] += 1
        for i in t:
            dct[i] -= 1
        for val in dct.values():
            if val != 0:
                return False
        return True
