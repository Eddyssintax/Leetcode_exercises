class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)
        d = {}

        for x in common:
            d[x] = list1.index(x) + list2.index(x)
        min_idx = min(d.values())
        op = []

        for i in d:
            if d[i] == min_idx:
                op.append(i)
        return op
