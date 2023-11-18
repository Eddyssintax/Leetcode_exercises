# using hash-map
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dct = {}

        for num in nums:
            if num in dct and dct[num] >= 1:
                return True
            dct[num] = dct.get(num, 0) + 1
        return False

# using simple compare


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(sen(nums))
